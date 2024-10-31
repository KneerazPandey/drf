from rest_framework import generics, mixins
from . models import Product
from . serializers import ProductSerializer
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404



class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    

class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    
    def perform_update(self, serializer):
        instance = serializer.save()
        return instance
    
class ProductDestroyAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    
    def perform_destroy(self, instance):
        return super().perform_destroy(instance)


class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'


class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    def perform_create(self, serializer):
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content')
        if not content:
            content=title 
        return serializer.save(content=content)
    

@api_view(http_method_names=['GET', 'POST'])    
def function_based_list_create_detail_view(request: Request, pk=None):
    if request.method == 'POST':
        serializer = ProductSerializer(data=request.data) 
        if serializer.is_valid():
            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('content')
            if not content:
                content = title
            serializer.save(content=content)
            return Response(data=serializer.data, status=status.HTTP_201_CREATEDF)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'GET':
        if pk is not None:
            obj = get_object_or_404(Product, pk=pk)
            # product = Product.objects.get(pk=pk)
            serializer = ProductSerializer(obj)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    else:
        return Response(data={'error': 'Invalid http methods'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
    
    
class ProductMixinView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    generics.GenericAPIView
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    
    def get(self, request: Request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk is not None:
            return self.retrieve(request, args, kwargs)
        return self.list(request, args, kwargs)
    
    def post(self, request: Request, *args, **kwargs):
        return self.create(request, args, kwargs)
    
    def perform_create(self, serializer):
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content')
        if not content:
            content = title
            
        return serializer.save(content=content)