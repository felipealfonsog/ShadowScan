import os
from utils import detect_suspicious_patterns

def scan_directory(directory):
    """Scans files in a directory for suspicious patterns"""
    results = []
    
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                with open(file_path, "r", errors="ignore") as f:
                    content = f.read()
                matches = detect_suspicious_patterns(content)
                if matches:
                    results.append({"file": file_path, "matches": matches})
            except Exception as e:
                print(f"Error reading {file_path}: {e}")

    return results
