## ShadowScan

## Overview
ShadowScan is a security tool designed to scan files and system configurations for hidden backdoors, malicious scripts, and reverse shells on Linux and macOS.

ShadowScan is an open-source cybersecurity tool built for penetration testers, system administrators, and security researchers.
It performs a deep scan of system files, looking for patterns commonly used in backdoors, malware, and reverse shells.
The tool is optimized for Linux distributions (Arch, Debian, Ubuntu, Fedora, etc.) and macOS, making it a lightweight but powerful security solution.

### Main Features:

    ✔ Detects hidden backdoors in shell scripts (.bashrc, .bash_profile, cron jobs).
    ✔ Scans for reverse shells, common obfuscation techniques, and suspicious commands (nc -e, python -c 'import pty').
    ✔ Integrates with VirusTotal and other threat intelligence APIs for checking unknown binaries.
    ✔ Identifies unauthorized SSH keys and altered system configurations.
    ✔ Creates a detailed security report highlighting the most critical findings.

#

## Installation
### Requirements
- Python 3.8+
- Dependencies listed in `requirements.txt`

### Setup
```bash
git clone https://github.com/yourusername/ShadowScan.git
cd ShadowScan
pip install -r requirements.txt
```

## Usage
### Basic Scan
```bash
python src/shadowscan.py --scan /path/to/directory
```

### Scan with VirusTotal
```bash
python src/shadowscan.py --scan /path/to/directory --virustotal YOUR_API_KEY
```

### Generate a Report
```bash
python src/shadowscan.py --scan /path/to/directory --report output.json
```

## Contribution
1. Fork the repository.
2. Create a new branch.
3. Commit your changes.
4. Submit a pull request.

## License
ShadowScan is licensed under the BSD 3-clause

