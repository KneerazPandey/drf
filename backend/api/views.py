import json
from django.http import HttpRequest, JsonResponse


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