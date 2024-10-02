from django.urls import path
from . views import api_home, api_product, new_api_home_rest_api, api_home_with_response_from_serializer


urlpatterns = [
    path('', api_home_with_response_from_serializer, name='api-home'),
    path('product/', api_product, name='api-product'),
]
