

import time
import re
import signal
import sys

def parse_log_entry(entry):
  
    pattern = r'(\d+\.\d+\.\d+\.\d+).*?(Success|Failed)'
    match = re.search(pattern, entry)
    if match:
        return match.group(1), match.group(2)
    else:
        return None, None

def analyze_log_entry(ip, status):
    if status == "Failed":
        failed_login_count[ip] = failed_login_count.get(ip, 0) + 1
        if failed_login_count[ip] >= MAX_FAILED_LOGIN_ATTEMPTS:
            print(f"Alert: Multiple failed login attempts detected from {ip}")
def monitor_log_file(log_file):
    with open(log_file, 'r') as f:

        f.seek(0, 2)
        while True:
            line = f.readline()
            if line:
                ip, status = parse_log_entry(line)
                if ip and status:
                    analyze_log_entry(ip, status)
            else:
                time.sleep(0.1)

# Constants
LOG_FILE = "web_server.log"
MAX_FAILED_LOGIN_ATTEMPTS = 3

failed_login_count = {}

def signal_handler(sig, frame):
    print("Monitoring stopped by user.")
    sys.exit(0)

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    print("Monitoring log file...")
    monitor_log_file(LOG_FILE)
