import region
import weather

region_code, area_code = region.get_centers_dict()["北海道地方"]["石狩・空知・後志地方"]["石狩地方"]
print(weather.get_weather(region_code, area_code))