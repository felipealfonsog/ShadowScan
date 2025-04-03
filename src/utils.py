import json

def load_rules():
    with open('rules.json', 'r') as f:
        rules = json.load(f)
    return rules

def detect_suspicious_patterns(content):
    rules = load_rules()
    suspicious_patterns = []
    for rule in rules['suspicious_keywords']:
        if rule in content:
            suspicious_patterns.append(rule)
    return suspicious_patterns
