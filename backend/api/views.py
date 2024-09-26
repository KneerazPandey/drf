import json
from django.http import HttpRequest, JsonResponse, HttpResponse
from products.models import Product
from django.forms.models import model_to_dict


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