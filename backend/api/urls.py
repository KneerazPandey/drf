from django.urls import path
from . views import api_home, api_product, new_api_home_rest_api


urlpatterns = [
    path('', new_api_home_rest_api, name='api-home'),
    path('product/', api_product, name='api-product'),
]
