import requests

url = "https://currency-converter5.p.rapidapi.com/currency/convert"

querystring = {"format":"json","from":"USD","to":"GHS","amount":"1"}

headers = {
    'x-rapidapi-host': "currency-converter5.p.rapidapi.com",
    'x-rapidapi-key': "a6a9fd82ebmsh8ec3ffdb68ee793p1d8552jsn7d73ba862a42"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)