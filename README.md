# Port Scanner
A simple Python-based Port Scanner that scans a target IP for open ports. This tool is useful for learning about networking and security scanning techniques.

## Features
✔️ Scans a range of ports on a target IP/hostname

✔️ Uses Python’s built-in `socket` module

✔️ Displays open ports in real-time

✔️ Easy to use and beginner-friendly

## Installation & Usage

**Step 1:** Clone the Repository
If you haven't already cloned the repository from GitHub, run:
```
git clone https://github.com/YOUR_GITHUB_USERNAME/port-scanner.git
cd port-scanner
```

**Step 2:** Run the Script
Make sure you have Python installed, then run:
```
python port_scanner.py
```

**Step 3:** Enter Target Details
The script will prompt you to enter:
- Target IP or Hostname (e.g., `scanme.nmap.org`)
- Start Port (e.g., `1`)
- End Port (e.g., `1000`)
Example:
```
Enter target IP or hostname: scanme.nmap.org  
Enter start port: 1  
Enter end port: 1000  
```
![Port Scanner in Action]("D:/Projects/PortScanner/Screenshots/screenshot1.png")

## How It Works
1. The script takes an IP address or Hostname as input.
2. It attempts to connect to each port in the specified range.
3. If a port is open, it prints "Port X is open".
4. If a port is closed, it prints Error scanning Port X: timed out, Port is closed.

## Disclaimer
**⚠️ This tool is intended for educational purposes only. Do not use it to scan networks or systems without permission. Unauthorized scanning may be illegal.**

## Contributing
Want to improve this project? Feel free to:
✅ Add multi-threading for faster scanning
✅ Enhance the output format
✅ Save scan results to a file

Fork this repo and submit a pull request!

## Contact
Got questions? Reach out to me via **GitHub Issues** or **email**!