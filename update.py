import urllib.request, json

urls = [
    "https://ez-pp.farm/api/get_player_info?id=23848&scope=stats",
    "https://ez-pp.farm/api/get_player_info?name=Hu+Tae&scope=stats",
    "https://ez-pp.farm/api/get_player_stats?id=23848",
    "https://ez-pp.farm/api/get_player_scores?id=23848&scope=best",
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
