import requests

endpoint = 'http://localhost:8000/api/'

get_response = requests.get(endpoint, params={"test" : "helloworld"}, json={"id" : "Long"})

print(get_response.json())