import psutil
import sys

def RunningSpecificProcessInfo(ProcessName):
    print(f"{'PID':<10} {'Process-Name':<35} {'User-Name'}")
    print("="* 60)
    for proc in psutil.process_iter():
        info = proc.as_dict(attrs=['pid','name','username'])
        if ProcessName.lower() == info['name'].lower():
            print(f"{info['pid']:<10} {info['name']:<35} {info['username']}")#value:< width--> format specifiers

def main():
    if len(sys.argv) != 2:
        print("Invalid number of arguments.")
        print("Use --h for help or --u for usage.")
        return

    if sys.argv[1].lower() == "--h":
        print("This script displays information (PID, name, username) of a running process.")
        print("Provide the process name as an argument.")
    elif sys.argv[1].lower() == "--u":
        print("Usage:")
        print("  python3 script_name.py <ProcessName>")
        print("Example:")
        print("  python3 script_name.py chrome")
    else:
        RunningSpecificProcessInfo(sys.argv[1])
    

if __name__ == "__main__":
    main()


