import json

def load_config():
    with open("data.json", "r", encoding="utf-8") as f:
        return json.load(f)["developer"] 