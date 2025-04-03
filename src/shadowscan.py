import sys
import os

# Add the src directory to sys.path for module imports
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

import argparse
from scanner import scan_directory
from report import generate_report  # This will now look for the report.py file in the src folder

def main():
    parser = argparse.ArgumentParser(description="ShadowScan - Detect hidden backdoors and malicious scripts.")
    parser.add_argument("--scan", required=True, help="Directory to scan")
    parser.add_argument("--report", help="Save report to a JSON file")
    parser.add_argument("--virustotal", help="VirusTotal API key for binary analysis")
    
    args = parser.parse_args()
    scan_results = scan_directory(args.scan, args.virustotal)
    
    if args.report:
        generate_report(scan_results, args.report)
    else:
        print(scan_results)

if __name__ == "__main__":
    main()
