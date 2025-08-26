import json

with open("skills.json", "r", encoding="utf-8") as file:
    data = json.load(file)

for category in data["skills"]:
    for skill in data["skills"][category]:
        print(skill["name"])
        print()