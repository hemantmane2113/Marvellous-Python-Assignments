import sys
import os
import shutil

def ExtensionExtract(DirectoryName1,DirectoryName2):

    flag = os.path.isabs(DirectoryName1)

    if flag == False:#updater
        DirectoryName1 = os.path.abspath(DirectoryName1)

    flag = os.path.exists(DirectoryName1)

    if(flag == False):#filter
        print("The path is invalid")
        exit()

    flag = os.path.isdir(DirectoryName1)

    if(flag == False):#filter
        print("Path is valid but target is not directory.")
        exit()

    New_Directory = DirectoryName2
    os.mkdir(New_Directory)

    flag = os.path.isabs(DirectoryName2)

    if flag == False:#updater
        DirectoryName2 = os.path.abspath(DirectoryName2)

    flag = os.path.exists(DirectoryName2)

    if(flag == False):#filter
        print("The path is invalid")
        exit()

    flag = os.path.isdir(DirectoryName2)

    if(flag == False):#filter
        print("Path is valid but target is not directory.")
        exit()

    print(print("Absolute path of new directory is :"+DirectoryName2))

    copied_files = []
    for FolderName,SubFolderNames,FileNames in os.walk(DirectoryName1):
        for fname in FileNames:
            src_path = os.path.join(DirectoryName1, fname)
            dst_path = os.path.join(DirectoryName2, fname)
            shutil.copy(src_path,dst_path)
            copied_files.append(fname)

#shutil.copy copies files from one directory to other and not the whole directory.
# therefore enter the path of files and not the directories.
    if copied_files:# == if len(copied_files) > 0:
        print("Following files were copied: ")
        for file in copied_files:
            print(f"- {file}")
    else:
        print("No files were copied")
    

def main():

    if(len(sys.argv)== 3):
        ExtensionExtract(sys.argv[1],sys.argv[2])
    elif(len(sys.argv) == 2):
        if((sys.argv[1] == '--h') or(sys.argv[1] == '--H')):
            print("This application is used to copy the files from one directory to other directory")
            print("This is the automation script")
        elif((sys.argv[1] == '--u') or(sys.argv[1] == '--U')):
            print("Use the given script as -------")
            print("<ScriptName.py>  <Directory Name1>    <Directory Name12>  ")
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