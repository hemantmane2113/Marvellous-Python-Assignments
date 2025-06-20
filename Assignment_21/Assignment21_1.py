import psutil
import os

def RunningProcessInfo():
    print(f"{'PID':<10} {'Process-Name':<35} {'User-Name'}")
    print("="* 60)
    for proc in psutil.process_iter():
        info = proc.as_dict(attrs=['pid','name','username'])
        pid = info['pid']
        process = info['name']
        name = info['username']
        print(f"{pid:<10} {process:<35} {name}")#value:< width--> format specifiers


def main():
    print('The running processes are as follows: \n')
    RunningProcessInfo()

if __name__ == "__main__":
    main()

