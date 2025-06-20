import sys
import os
import hashlib

def CheckSum(DirectoryName,BlockSize = 1024):

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

    hexlist = []
    for FolderName,SubFolderNames,FileNames in os.walk(DirectoryName):
        for fname in FileNames:
            fobj = open((os.path.join(FolderName,fname)),'rb')## rb- read in binary

            hobj = hashlib.md5()

            buffer = fobj.read(BlockSize)

            while(len(buffer) > 0):
                hobj.update(buffer)

                buffer = fobj.read(BlockSize)


            fobj.close()
            hexlist.append((fname,hobj.hexdigest()))

    return hexlist
            


def main():
    argc  = len(sys.argv)

    if argc == 2:
        ret = CheckSum(sys.argv[1])
    elif argc == 3:
        try:
            blocksize = int(sys.argv[2])#sys.argv takes command in string format
        except ValueError:
            print("Enter the blocksize in integer")
            return
    
        ret = CheckSum(sys.argv[1],blocksize)
        

    elif(len(sys.argv) == 2):
        if((sys.argv[1] == '--h') or(sys.argv[1] == '--H')):
            print("This application is used to check the checksum of all the files in a given directory")
            print("This is the automation script")
        elif((sys.argv[1] == '--u') or(sys.argv[1] == '--U')):
            print("Use the given script as below-----------")
            print("<ScriptName.py>  <Directory Name> ")
        else:
            print("Use the given flags as: ")
            print("--h: Use to display the help")
            print("--u: Use to display the usage")
    else:
        print("Invalid number of arguements")
        print("Use the given flags as: ")
        print("--h: Use to display the help")
        print("--u: Use to display the usage")

    print('The checksum of the files in a directory are: ')
    for file,checksum in ret:
        print(f"{file}:{checksum}")


if __name__ == "__main__":
    main()