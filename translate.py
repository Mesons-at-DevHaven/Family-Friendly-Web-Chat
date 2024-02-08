import requests
import uuid
import http.client

def makeItSafe(text):
    key = "569dd2d3cd4a485da6a4291db504dc52"
    endpoint = "https://api.cognitive.microsofttranslator.com"
    conn = http.client.HTTPSConnection("community-purgomalum.p.rapidapi.com")

    headersRapidAPI = {
       'X-RapidAPI-Key': "481794fbaemshe39ee411326e351p16ca8ejsne151761862f3",
        'X-RapidAPI-Host': "community-purgomalum.p.rapidapi.com"
    }

    location = "southeastasia"

    path = '/translate'
    constructed_url = endpoint + path

    params = {
        'api-version': '3.0',
        'to': ['en']
    }

    headers = {
        'Ocp-Apim-Subscription-Key': key,
        'Ocp-Apim-Subscription-Region': location,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }

    textinput = input()
    body = [{
        'text': textinput
    }]

    request = requests.post(constructed_url, params=params, headers=headers, json=body)
    response = request.json()
    languageIN = response[0]['detectedLanguage']['language']

    params = {
        'api-version': '3.0',
        'from': languageIN,
        'to': ['en']
    }

    headers = {
        'Ocp-Apim-Subscription-Key': key,
        'Ocp-Apim-Subscription-Region': location,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }

    body = [{
        'text': textinput
    }]

    request = requests.post(constructed_url, params=params, headers=headers, json=body)
    response = request.json()
    texttoprof= response[0]['translations'][0]['text']
    texttoprof = texttoprof.replace(" ", "%20")

    conn.request("GET", "/json?text=" + texttoprof, headers=headersRapidAPI)

    res = conn.getresponse()
    data = res.read()
    datanew = data.decode("utf-8")
    dataout = datanew[11:-2]
    return dataout