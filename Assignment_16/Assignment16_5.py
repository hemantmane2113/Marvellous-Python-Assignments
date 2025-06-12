import os
import string


def File_Handling(Name_Of_File):

    ret = os.path.exists(Name_Of_File)

    if ret == True:
        print(f"File { Name_Of_File} exists.")

        fobj = open(Name_Of_File,'r')

        for line in fobj:
            words = line.split()
            if len(words) > 5:
                print(line)
                print()

    else:
        print(f"File { Name_Of_File} does not exists.")


def main():
    print("Enter the name of file: ")
    Fname = input()

    
    File_Handling(Fname)



if __name__ == "__main__":
    main()