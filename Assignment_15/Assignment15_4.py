import os
import sys

def File_Handling(Name_of_File_1,Name_of_File_2):
    
    ret1 = os.path.exists(Name_of_File_1)

    ret2 = os.path.exists(Name_of_File_2)

    if (ret1 == True):

        if(ret2 == True):
            print(f"The file {Name_of_File_1} and {Name_of_File_2} exists in the current directory.")

            fobj1 = open(Name_of_File_1,"r")

            data1  = fobj1.read()
            print(f"Data in the {Name_of_File_1 } is: ",data1)

            
            fobj2 = open(Name_of_File_2,"r")

            data2 = fobj2.read()
            print(f"Data in the {Name_of_File_2 } is: ",data2)

            if(data1 == data2):
                print(f"Successful")
            else:
                print("Failure")

        else:
            print(f"There is no such file by the name {Name_of_File_2} in the current directory.")
    
    else:
        print(f"There is no such file by the name {Name_of_File_1} in the current directory.")

    
def main():

    if(len(sys.argv) == 3):
        if((sys.argv[1] == '--h') or(sys.argv[1] == '--H')):
            print("This program is used to compare data of both the files.")
            
        elif((sys.argv[1] == '--u') or(sys.argv[1] == '--U')):
            print("Use the given script as -------")
            print("ScriptName.py  FileName1    FileName2")

        else:
             File_Handling(sys.argv[1],sys.argv[2])
            
        
    else:
        print("Invalid number of arguements")
        print("Use the given flags as: ")
        print("--h: Use to display the help")
        print("--u: Use to display the usage")

    




if __name__ == "__main__":
    main()