import sys

# IMPORT ALL YOUR TOOLS HERE:
from utils.password import check_password_strength
from utils.file_integrity import calculate_sha256
from utils.log_analyzer import parse_ssh_logs
from utils.scanner import scan_ports

def main_menu():
    print("\n" + "="*30)
    print("    SECURITY TOOLKIT (CLI)    ")
    print("="*30)
    print("1. Password Strength Checker")
    print("2. File Integrity Checker") 
    print("3. Log Analyzer")
    print("4. Port Scanner")
    print("5. Exit")
    print("="*30)
    
    choice = input("Select an option (1-5): ")
    return choice

if __name__ == "__main__":
    while True:
        choice = main_menu()
        
        # --- TOOL 1: PASSWORD CHECKER ---
        if choice == '1':
            print("\n--- Password Strength Checker ---")
            user_pwd = input("Enter a password to test: ")
            result = check_password_strength(user_pwd)
            print(f"Password Strength: {result}")
            
        # --- TOOL 2: FILE INTEGRITY CHECKER ---
        elif choice == '2':
            print("\n--- File Integrity Checker ---")
            path = input("Enter the path to the file to hash: ")
            hash_result = calculate_sha256(path)
            if hash_result:
                print(f"[+] SHA-256 Hash: {hash_result}")
            else:
                print("[-] File not found. Make sure the path is correct.")
            
        # --- TOOL 3: LOG ANALYZER ---
        elif choice == '3':
            print("\n--- SSH Log Analyzer ---")
            log_path = input("Enter path to log file (or press Enter for /var/log/auth.log): ").strip()
            if not log_path:
                log_path = "/var/log/auth.log"  # Default system log location on Debian/Ubuntu
            
            results = parse_ssh_logs(log_path)
            if results is not None:
                if results:
                    print("\n[+] Failed Login Attempts Found:")
                    print(f"{'IP Address':<20} | {'Failed Attempts':<15}")
                    print("-" * 38)
                    for ip, count in results.items():
                        print(f"{ip:<20} | {count:<15}")
                else:
                    print("[+] No failed SSH login attempts detected in this file.")

        # --- TOOL 4: PORT SCANNER ---
        elif choice == '4':
            print("\n--- Network Port Scanner ---")
            target = input("Enter target IP address or hostname (e.g., 127.0.0.1 or scanme.nmap.org): ")
            start_p = input("Enter start port (default 1): ")
            end_p = input("Enter end port (default 100): ")
            
            # Default values if user leaves them blank
            start_p = int(start_p) if start_p.isdigit() else 1
            end_p = int(end_p) if end_p.isdigit() else 100
            
            scan_ports(target, (start_p, end_p))

        # --- EXIT OPTION ---
        elif choice == '5':
            print("\nExiting Toolkit. Stay safe!")
            sys.exit()
            
        else:
            print("\n[-] Invalid option. Please enter 1-5.")
            
        input("\nPress Enter to return to menu...")