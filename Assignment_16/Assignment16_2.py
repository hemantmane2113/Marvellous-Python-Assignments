import os


def File_Handling(Name_Of_File = "data.txt"):

    ret = os.path.exists(Name_Of_File)

    if ret == True:
        print(f"File { Name_Of_File} exists.")

        fobj = open(Name_Of_File,'r')

        data = fobj.read()

        print("The data in file is :\n",data)

    else:
        print(f"File { Name_Of_File} does not exists.")
        

    


def main():
    
    File_Handling()



if __name__ == "__main__":
    main()