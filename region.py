import web_json

url = "https://www.jma.go.jp/bosai/common/const/area.json"
jsonData = web_json.get_json(url)

def get_centers_dict():
    centers_dict = {}
    for value in jsonData["centers"].values():
        centers_dict[value["name"]] = get_offices_dict(value["children"])
    return centers_dict

def get_offices_dict(offices_code):
    offices_dict = {}
    for office_code in offices_code:
        offices_dict[jsonData["offices"][office_code]["name"]] = get_class10s_dict(jsonData["offices"][office_code]["children"], office_code)
    return offices_dict

def get_class10s_dict(class10s_code, parent_code):
    class10s_dict = {}
    for class10_code in class10s_code:
        class10s_dict[jsonData["class10s"][class10_code]["name"]] = [parent_code, class10_code]
    return class10s_dict