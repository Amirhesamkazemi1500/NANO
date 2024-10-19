import os
import time

# Define colors
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

def print_header():
    header_length = 63
    title = "WELCOME TO THE TERMINAL SIMULATOR"
    padding_length = (header_length - len(title)) // 2
    
    print(f"{Colors.HEADER}{'=' * header_length}{Colors.ENDC}")
    print(f"{Colors.OKGREEN}{' ' * padding_length}{title}{' ' * padding_length}{Colors.ENDC}")
    print(f"{Colors.HEADER}{'=' * header_length}{Colors.ENDC}")

def print_status(message):
    print(f"{Colors.OKBLUE}[INFO] {message}{Colors.ENDC}")

def print_report(report_message):
    print(f"{Colors.WARNING}┌─[update@termux]─[~/nano]{Colors.ENDC}")
    print(f"{Colors.WARNING}└──╼ ❯❯❯ {report_message}{Colors.ENDC}")

def show_help():
    help_text = """
Available Commands:
- u : Execute 'git pull origin main'
- h : Show this help message
- q : Clear the terminal and exit after a few seconds
"""
    print(help_text)

def clear_and_exit():
    print_status("Clearing the terminal...")
    os.system("clear")  # Clear the terminal
    time.sleep(3)  # Wait for 3 seconds
    print_status("Exiting the terminal simulator.")
    exit()  # Exit the program

def main():
    os.system("clear")  # Clear the terminal at the start
    print_header()
    
    while True:
        command = input(f"{Colors.WARNING}Enter command (u for update, h for help, q to clear and exit): {Colors.ENDC}").strip().lower()
        
        if command == 'u':
            print_status("Executing 'git pull origin main'...")
            os.system("git pull origin main")
            print_status("Command executed successfully.")
            print_report("Report: Operation completed successfully.")
        
        elif command == 'h':
            show_help()
        
        elif command == 'q':
            clear_and_exit()
        
        else:
            print(f"{Colors.FAIL}[ERROR] Invalid command! Type 'h' for help.{Colors.ENDC}")

if __name__ == "__main__":
    main()
