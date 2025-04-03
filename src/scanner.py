# scanner.py
import os
import json
from utils import detect_suspicious_patterns

def scan_directory(directory, virustotal_key=None):
    results = []
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, 'r', errors='ignore') as f:
                content = f.read()
                matches = detect_suspicious_patterns(content)
                if matches:
                    results.append({"file": file_path, "matches": matches})
    return results

# report.py
import json

def generate_report(results, output_file):
    with open(output_file, "w") as f:
        json.dump(results, f, indent=4)
    print(f"Report saved to {output_file}")