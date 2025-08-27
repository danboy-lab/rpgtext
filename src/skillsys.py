import json
import os

# Get the path to the data directory
current_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(os.path.dirname(current_dir), "data")
skills_path = os.path.join(data_dir, "skills.json")

with open(skills_path, "r", encoding="utf-8") as file:
    data = json.load(file)

for category in data["skills"]:
    for skill in data["skills"][category]:
        skill["name"]