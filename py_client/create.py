import requests

endpoints = 'http://localhost:8000/api/products/'

data = {
    'title': 'Fourth Title'
}

response = requests.post(endpoints, json=data)


print(response)