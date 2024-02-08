import http.client

conn = http.client.HTTPSConnection("community-purgomalum.p.rapidapi.com")

headers = {
    'X-RapidAPI-Key': "481794fbaemshe39ee411326e351p16ca8ejsne151761862f3",
    'X-RapidAPI-Host': "community-purgomalum.p.rapidapi.com"
}

text = input("Enter the text: ")
text = text.replace(" ", "%20")


conn.request("GET", "/json?text=" + text, headers=headers)

res = conn.getresponse()
data = res.read()
datanew = data.decode("utf-8")
dataout = datanew[11:-2]
print(dataout)

