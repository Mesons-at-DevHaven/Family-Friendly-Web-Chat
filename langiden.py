import requests, uuid, json

# Add your key and endpoint
key = "569dd2d3cd4a485da6a4291db504dc52"
endpoint = "https://api.cognitive.microsofttranslator.com"

# location, also known as region.
# required if you're using a multi-service or regional (not global) resource. It can be found in the Azure portal on the Keys and Endpoint page.

location = "southeastasia"

path = '/detect'
constructed_url = endpoint + path

params = {
    'api-version': '3.0'
}

headers = {
    'Ocp-Apim-Subscription-Key': key,
    # location required if you're using a multi-service or regional (not global) resource.
    'Ocp-Apim-Subscription-Region': location,
    'Content-type': 'application/json',
    'X-ClientTraceId': str(uuid.uuid4())
}

textinput = input("Enter the text: ")

# You can pass more than one object in body.
body = [{
    'text': textinput
}]


request = requests.post(constructed_url, params=params, headers=headers, json=body)
response = request.json()

language = response[0]['language']
print(language)
