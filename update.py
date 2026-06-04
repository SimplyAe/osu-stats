import urllib.request, json

urls = [
    "https://new.ez-pp.farm/api/v1/users/23848",
    "https://new.ez-pp.farm/api/v1/player?id=23848",
    "https://new.ez-pp.farm/api/v1/stats?id=23848",
    "https://ez-pp.farm/api/v2/users/23848",
    "https://ez-pp.farm/api/v2/users/stats?id=23848",
]

for url in urls:
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req) as r:
            print(f"Success: {url}")
            print(r.read().decode()[:500])
            break
    except Exception as e:
        print(f"Failed {url}: {e}")
