import urllib.request, json

urls = [
    "https://ez-pp.farm/api/get_user?u=23848&type=id",
    "https://ez-pp.farm/api/get_user?u=Hu+Tae&type=string",
    "https://ez-pp.farm/api/v1/get_user?id=23848",
    "https://ez-pp.farm/api/player/info?id=23848",
    "https://ez-pp.farm/api/player/info?name=Hu+Tae",
]

for url in urls:
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req) as r:
            data = json.loads(r.read())
            print(f"Success: {url}")
            print(json.dumps(data, indent=2))
            break
    except Exception as e:
        print(f"Failed {url}: {e}")
