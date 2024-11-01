import json

inf = open("allcookies.json")

of = open("cookies_stripped.json", "w")

cooks = json.load(inf)
cooksdic = {}

for i in cooks:
    if i["name"][:4] == "ESTS":
        print(i["name"], i["value"], "\n")
        cooksdic[i["name"]] = i["value"]
        
json.dump(cooksdic, of)