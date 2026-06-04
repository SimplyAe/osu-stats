import urllib.request, json

urls = [
    "https://ez-pp.farm/api/v1/users/stats?id=23848&mode=0&relax=1",
    "https://ez-pp.farm/api/v1/users/full?id=23848",
]

data = None
for url in urls:
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req) as r:
            data = json.loads(r.read())
            print(f"Success with: {url}")
            print(json.dumps(data, indent=2))
            break
    except Exception as e:
        print(f"Failed {url}: {e}")

if data is None:
    print("All endpoints failed")
