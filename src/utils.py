import json

def load_rules():
    """Loads rules from rules.json"""
    try:
        with open("./src/rules.json", "r") as f:
            rules = json.load(f)
        return rules
    except FileNotFoundError:
        print("Error: rules.json not found.")
        return {"suspicious_keywords": []}

def detect_suspicious_patterns(content):
    """Detects suspicious patterns in the given content"""
    rules = load_rules()
    suspicious_patterns = []
    for rule in rules.get("suspicious_keywords", []):
        if rule in content:
            suspicious_patterns.append(rule)
    return suspicious_patterns
