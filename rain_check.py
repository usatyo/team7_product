
region_code, area_code = region.get_centers_dict()["北海道地方"]["石狩・空知・後志地方"]["石狩地方"]
weather_str = weather.get_weather(region_code, area_code)
def rain_check():
    if '雨' in weather_str:
        return True
    else:
        return False
