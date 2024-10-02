import json
from django.http import HttpRequest, JsonResponse
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import api_view
from products.models import Product
from django.forms.models import model_to_dict
from rest_framework import status
from products.serializers import ProductSerializer


def api_home(request: HttpRequest):
    print(request.GET) # getting url query params
    print(request.POST)
    print(request.body) # getting byte string of JSON data
    data = {}
    try:
        data = json.loads(request.body)
    except:
        pass
    data['params'] = dict(request.GET) 
    data['headers'] = dict(request.headers)
    data['content-type'] = request.content_type
    return JsonResponse(data)


def api_product(request: HttpRequest):
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
        # data['id'] = model_data.pk
        # data['title'] = model_data.title 
        # data['content'] = model_data.content
        # data['price'] = model_data.price
        data = model_to_dict(model_data, fields=['id', 'title'])
    return JsonResponse(data)
    #     data = model_to_dict(model_data, fields=['id', 'title'])
    #     data = json.dumps(data)
    # return HttpResponse(data, headers={'content-type': 'application/json'})
    
    
@api_view(["GET"])
def new_api_home_rest_api(request: Request):
    '''This is the simple Django REST API View'''
    model_data = Product.objects.all().order_by('?').first()
    data = {}
    if model_data:
        data = model_to_dict(model_data)
    
    return Response(data=data)


@api_view(['GET'])
def api_home_with_response_from_serializer(request: Request):
    model_data = Product.objects.all().order_by('?').first()
    serializer = ProductSerializer(model_data)
    return Response(data=serializer.data)