import sys
import os

def ExtensionExtract(DirectoryName,Ext_Name1,Ext_Name2):

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



    New_Ext_Files = []
    for FolderName,SubFolderNames,FileNames in os.walk(DirectoryName):
        for fname in FileNames:
           fname = fname.replace(Ext_Name1,Ext_Name2)
           New_Ext_Files.append(fname)
    
    if New_Ext_Files:
        print("The files with changed extensions are: ")
        for files in New_Ext_Files:
            print(files,end = " ")
            print()
    else:
        print("There are no files in the directory.")
        

def main():

    if(len(sys.argv)== 4):
        ExtensionExtract(sys.argv[1],sys.argv[2],sys.argv[3])
    elif(len(sys.argv) == 2):
        if((sys.argv[1] == '--h') or(sys.argv[1] == '--H')):
            print("This application is used to convert the files from one extension with other extension")
            print("This is the automation script")
        elif((sys.argv[1] == '--u') or(sys.argv[1] == '--U')):
            print("Use the given script as -------")
            print("<ScriptName.py>  <Directory Name>    <Extension Name1>  <Extension Name2 ")
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