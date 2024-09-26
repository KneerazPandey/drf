from django.urls import path
from . views import api_home, api_product


urlpatterns = [
    # path('', api_home, name='api-home'),
    path('', api_product, name='api-product'),
]
