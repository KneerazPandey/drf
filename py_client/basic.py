import requests

# endpoint = 'https://httpbin.org/anything'
endpoint = 'http://localhost:8000/api/'

# API -> Application Programming Interface.
# Http Request (Not API Request) -> HTML -> Just made for the browser.
# Rest API -> Json, Xml -> Can communicate with other different applications.

# Sending Http Requests to the endpoint 
# response = requests.get(endpoint)

# Passing an own json data to requests.
response = requests.post(
    endpoint, 
    json={'title': 'Second Product', 'content': 'Second Post Content'}
)
#? Note: The (data) can be obtained in django with request.body and in DRF with request.data
#? Note: The (?query or params) can be obtained in django with request.GET and in DRF with request.query_params

print(f'The status code is: {response.status_code}')
print(response.json())