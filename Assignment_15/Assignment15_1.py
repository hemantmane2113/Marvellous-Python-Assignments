import os

def File_Handling(Name_of_File):
    
    ret = os.path.exists(Name_of_File)

    if (ret == True):
        print(f"The file {Name_of_File} exists in the current directory.")
    else:
        print("There is no such file in the current directory.")


def main():
    print("Enter the file name that you want to check: \n")
    FileName = input()

    File_Handling(FileName)


if __name__ == "__main__":
    main()