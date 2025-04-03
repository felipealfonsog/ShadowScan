import argparse
from scanner import scan_directory
from report import generate_report

def main():
    parser = argparse.ArgumentParser(description="ShadowScan - File scanner for suspicious patterns")
    parser.add_argument("--scan", help="Directory to scan", required=True)
    parser.add_argument("--report", help="Save results to a report file", action="store_true")
    args = parser.parse_args()

    scan_results = scan_directory(args.scan)

    if scan_results:
        print("\n🔍 Scan Results:")
        for result in scan_results:
            print(f"\nFile: {result['file']}")
            print(f"Matches: {', '.join(result['matches'])}")
    else:
        print("✅ No suspicious matches found.")

    # Save report if requested
    if args.report:
        generate_report(scan_results)

if __name__ == "__main__":
    main()
