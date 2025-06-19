import os

def FileExits(FileName):

    Fpath = os.path.abspath(FileName)


    ret = os.path.exists(Fpath)

    if ret == True:
        return True
    else:
        return False

def main():

    print("Enter the file name: ")
    FName = input()


    ret = FileExits(FName)

    if ret == True:
        print(f"The file {FName} exists in the current directory.")
    else:
        print(f"The file {FName} does not exists in the current directory.")


if __name__ == "__main__":
    main()