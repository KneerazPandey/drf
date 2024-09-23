import requests

endpoint = 'https://httpbin.org/anything'

# API -> Application Programming Interface.
# Http Request (Not API Request) -> HTML -> Just made for the browser.
# Rest API -> Json, Xml -> Can communicate with other different applications.

# Sending Http Requests to the endpoint 
# response = requests.get(endpoint)

# Passing an own json data to requests.
response = requests.get(endpoint, json={'name': 'Niraj Pandey'}, data={'image': 'this is form data'})

print(f'The status code is: {response.status_code}')
print(response.json())