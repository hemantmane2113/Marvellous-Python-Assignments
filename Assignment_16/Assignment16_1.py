import os


def File_Handling(Name_Of_File,List_Of_Names):

    fobj = open(Name_Of_File,'w+') # write + read
    

    ret = os.path.exists(Name_Of_File)

    if ret == True:
        print(f"File is successfully created by the name {Name_Of_File}")
    else:
        print("No such file exists.")

    counter = 1
    for name in List_Of_Names:
            fobj.write(str(counter) + ". " + name + "\n")
            counter = counter + 1

    fobj.seek(0)## to read the file,we need to bring back cursor at the  start of line if 
    #names are printed one after the other and not to the new line.
    data = fobj.read()

    if data == List_Of_Names:
        print(f"Data is successfully entered into the file {Name_Of_File}")

    fobj.close()

    
def main():


    print("Enter the name of file you want to create:  \n")
    FileName = input()

    print("Enter how many names you want to enter: ")
    iValue = int(input())

    NameList = []

    for i in range(1,iValue+1):
        print(f"Enter name {i}: ")
        name = input()
        NameList.append(name)

    File_Handling(FileName,NameList)


if __name__ == "__main__":
    main()