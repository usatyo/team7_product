import web_json

def get_weather(office_code, area_code):
    url = f"https://www.jma.go.jp/bosai/forecast/data/forecast/{office_code}.json"
    jsonData = web_json.get_json(url)
    for area_json in jsonData[0]["timeSeries"][0]["areas"]:
        if area_json["area"]["code"] == area_code:
            return area_json["weathers"][0]