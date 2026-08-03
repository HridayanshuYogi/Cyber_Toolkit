import os
import re

def parse_ssh_logs(log_path):
    """
    Parses SSH authentication logs to find failed login attempts 
    and groups them by IP address.
    """
    if not os.path.exists(log_path):
        print("[-] Error: Log file does not exist.")
        return None

    failed_ip_counts = {}

    try:
        with open(log_path, 'r', encoding='utf-8', errors='ignore') as f:
            for line in f:
                # Look for lines containing "Failed password"
                if "Failed password" in line:
                    # Regular expression to extract the IP address
                    ip_match = re.search(r'from\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', line)
                    if ip_match:
                        ip = ip_match.group(1)
                        failed_ip_counts[ip] = failed_ip_counts.get(ip, 0) + 1

        return failed_ip_counts

    except Exception as e:
        print(f"[-] Error reading log file: {e}")
        return None
