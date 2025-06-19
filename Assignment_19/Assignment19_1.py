import sys
import os

def ExtensionExtract(DirectoryName,Ext_Name):

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

    #print("Absolute path is :"+DirectoryName)


    Text_Files = []
    for FolderName,SubFolderNames,FileNames in os.walk(DirectoryName):
        for fname in FileNames:
           if fname.endswith(Ext_Name):
               Text_Files.append(fname)
    if Text_Files:
        print(f"The files in the Directory {DirectoryName} with extension {Ext_Name} are: ")      
        for file in Text_Files:
            print(file,end = " ")
            print()
    else:
        print(f"There are no files in the directory {DirectoryName} with extension {Ext_Name}")          

def main():

    if(len(sys.argv)== 3):
        ExtensionExtract(sys.argv[1],sys.argv[2])
    elif(len(sys.argv) == 2):
        if((sys.argv[1] == '--h') or(sys.argv[1] == '--H')):
            print("This application is used to find the files with given extension")
            print("This is the automation script")
        elif((sys.argv[1] == '--u') or(sys.argv[1] == '--U')):
            print("Use the given script as -------")
            print("<ScriptName.py>  <Directory Name>    <Extension Name> ")
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