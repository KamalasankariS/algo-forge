import json
import sys

commit = sys.argv[1].lower()

with open("data/xp.json") as f:
    data = json.load(f)

xp_map = {
    "easy":15,
    "medium":30,
    "hard":50,
    "topic":65,
    "system":100
}

for key in xp_map:
    if commit.startswith(key):

        data["xp"] += xp_map[key]
        data[key + "s"] += 1

level = data["level"]
xp_required = level * 100

if data["xp"] >= xp_required:
    data["xp"] -= xp_required
    data["level"] += 1

with open("data/xp.json","w") as f:
    json.dump(data,f,indent=2)