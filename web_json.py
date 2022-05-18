import requests

def get_json(url):
    headers = {"content-type": "application/json"}
    response = requests.get(url, headers=headers)
    response.encoding = response.apparent_encoding
    return response.json()