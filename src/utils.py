import json
import os

def load_rules():
    """Loads suspicious patterns from rules.json"""
    rules_path = os.path.join(os.path.dirname(__file__), "rules.json")

    if not os.path.exists(rules_path):
        print("Error: rules.json not found.")
        return []

    try:
        with open(rules_path, "r") as f:
            data = json.load(f)
            return data.get("suspicious_patterns", [])
    except Exception as e:
        print(f"Error loading rules.json: {e}")
        return []

def detect_suspicious_patterns(content):
    """Detects suspicious patterns in file content"""
    rules = load_rules()
    return [rule for rule in rules if rule in content]
