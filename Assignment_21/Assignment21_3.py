import psutil
import os
import sys
from datetime import datetime

def DirectoryWatcher(DirectoryName):
    flag = os.path.isabs(DirectoryName)

    if flag == False:#updater
        DirectoryName = os.path.abspath(DirectoryName)

    flag = os.path.exists(DirectoryName)

    if(flag == False):#filter
        print("The path is invalid")
        exit()

    flag = os.path.isdir(DirectoryName)

    if(flag == False):#filter
        print("Path is valid but target is not directory.")
        exit()

    log_path = os.path.join(DirectoryName, "ProcessLog.txt")
    return log_path
    
def RunningProcessInfoLog(log_path):
    header = f"{'PID':<10} {'Process-Name':<35} {'User-Name'}"
    separator = "=" * 60
    
    
    fobj = open(log_path,'w')
    fobj.write("Process Log Generated on: " + str(datetime.now()) + "\n")
    fobj.write(header + "\n")
    fobj.write(separator + "\n")

    for proc in psutil.process_iter():
        info = proc.as_dict(attrs=['pid','name','username'])
        pid = info['pid']
        process = info['name']
        name = info['username']
        line = f"{pid:<10} {process:<35} {name}"
        fobj.write(line+"\n")


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
        ret1 = DirectoryWatcher(sys.argv[1])

        RunningProcessInfoLog(ret1)
        print(f"\nLog file has been saved to: {ret1}")



if __name__ == "__main__":
    main()

