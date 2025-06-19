import sys
import os


def Compare(FName1,FName2):
    ret1 = os.path.exists(FName1)
    ret2 = os.path.exists(FName2)
    

    if ret1 == True:
        fobj1 = open(FName1,'r')

        data1 = fobj1.read()

        if ret2 == True:

            fobj2 = open(FName2,'r')

            data2 = fobj2.read()

        else:
            print(f"{FName2} does not exists.")
            return None
    
    else:
        print(f"{FName1} does not exist.")
        return None
    
    if data1 == data2:
        return True
    else:
        return False
    
    
     
def main():
    if(len(sys.argv) == 3):
        ret = Compare(sys.argv[1],sys.argv[2])
        if ret == True:
            print("Sucess")
        else:
            print("Failure")
    elif(len(sys.argv) == 2):
        if((sys.argv[1] == '--h') or(sys.argv[1] == '--H')):
            print("This application is used to compare contents of one file with other.")
        elif((sys.argv[1] == '--u') or(sys.argv[1] == '--U')):
            print("Use the given script as -------")
            print("ScriptName.py  File1   File2")
                  
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