from rest_framework import serializers
from . models import Product


class ProductSerializer(serializers.ModelSerializer):
    discount_percent = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Product
        fields = ['id', 'title', 'price', 'content', 'sale_price', 'discount_percent']
        
    def get_discount_percent(self, obj):
        return obj.get_discount() 