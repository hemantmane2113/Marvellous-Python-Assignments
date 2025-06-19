import sys
import os


def ChckFreq(FName1,Strr):
    ret1 = os.path.exists(FName1)
    
    if ret1 == True:
        fobj1 = open(FName1,'r')

        data = fobj1.read()

        listt = data.split(".")

        cleaned_list = []

        for part in listt:
            part = part.strip()
            if part:
                cleaned_list.append(part)
    else:
        print(f"{FName1} does not exists.")
        
    counter = 0
    for content in cleaned_list:
        if Strr.lower() == content.lower():
            counter = counter + 1

    return counter

def main():
    if(len(sys.argv) == 3):
        ret = ChckFreq(sys.argv[1],sys.argv[2])
        print(f"{sys.argv[2]} occured {ret} times in the file {sys.argv[1]}")
    elif(len(sys.argv) == 2):
        if((sys.argv[1] == '--h') or(sys.argv[1] == '--H')):
            print("This application is used to check the frequency of string in a file.")
        elif((sys.argv[1] == '--u') or(sys.argv[1] == '--U')):
            print("Use the given script as -------")
            print("ScriptName.py  File    String")
                  
        else:
            print("Use the given flags as: ")
            print("--h: Use to display the help")
            print("--u: Use to display the usage")
    else:
        print("Invalid number of arguements")
        print("Use the given flags as: ")
        print("--h: Use to display the help")
        print("--u: Use to display the usage")

    
if __name__ == "__main__":
    main()