# utils.py
import json

def load_rules():
    with open("rules.json", "r") as f:
        return json.load(f)

def detect_suspicious_patterns(content):
    rules = load_rules()
    matches = []
    for rule in rules:
        if rule["pattern"] in content:
            matches.append(rule)
    return matches