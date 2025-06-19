import sys
import os


def Copy(FName1,FName2):
    ret1 = os.path.exists(FName1)
    

    if ret1 == True:
        fobj1 = open(FName1,'r')

        data1 = fobj1.read()

        fobj2 = open(FName2,'w+')

        fobj2.write(data1)

        fobj2.seek(0)## to bring the  cursor back to starting point

        data2 = fobj2.read()

        return data2
    
    else:
        print(f"{FName1} does not exist.")
        return -1
     
def main():
    if(len(sys.argv) == 3):
        ret = Copy(sys.argv[1],sys.argv[2])
        if ret != -1:
            print(f"The content copied in the {sys.argv[2]} is as given below: \n",ret) 
    elif(len(sys.argv) == 2):
        if((sys.argv[1] == '--h') or(sys.argv[1] == '--H')):
            print("This application is used to copy content from one file to another.")
        elif((sys.argv[1] == '--u') or(sys.argv[1] == '--U')):
            print("Use the given script as -------")
            print("ScriptName.py  File to copy    File to be copied")
                  
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