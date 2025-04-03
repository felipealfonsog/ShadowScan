import json

def generate_report(scan_results, output_file):
    """Generates a report from the scan results and saves it to a JSON file."""
    with open(output_file, 'w') as report_file:
        json.dump(scan_results, report_file, indent=4)
    print(f"Report saved to {output_file}")
