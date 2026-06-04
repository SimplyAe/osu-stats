import urllib.request, json

url = "https://ez-pp.farm/api/v1/users/stats?id=23848&mode=0&relax=1"
with urllib.request.urlopen(url) as r:
    data = json.loads(r.read())

pp = round(data["pp"])

svg = (
    '<svg xmlns="http://www.w3.org/2000/svg" width="160" height="35">'
    '<rect width="160" height="35" rx="17" fill="#111111"/>'
    '<rect x="55" width="105" height="35" rx="17" fill="#00ECFF"/>'
    '<rect x="55" width="20" height="35" fill="#111111"/>'
    '<text x="27" y="23" font-family="Arial" font-size="13" font-weight="bold" fill="#00ECFF" text-anchor="middle">PP</text>'
    f'<text x="112" y="23" font-family="Arial" font-size="13" font-weight="bold" fill="#111111" text-anchor="middle">{pp}pp</text>'
    '</svg>'
)

with open("badge.svg", "w") as f:
    f.write(svg)

print(f"PP: {pp}")
