def generate_report(scan_results, output_file="scan_report.txt"):
    """Generates a report from scan results and saves it to a file"""
    try:
        with open(output_file, "w") as f:
            f.write("🔍 ShadowScan Report\n")
            f.write("=" * 50 + "\n\n")

            if not scan_results:
                f.write("✅ No suspicious matches found.\n")
            else:
                for result in scan_results:
                    f.write(f"File: {result['file']}\n")
                    f.write(f"Matches: {', '.join(result['matches'])}\n")
                    f.write("-" * 50 + "\n")

        print(f"📄 Report saved to {output_file}")
    except Exception as e:
        print(f"Error writing report: {e}")
