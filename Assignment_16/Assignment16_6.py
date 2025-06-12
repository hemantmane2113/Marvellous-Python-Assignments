import os

def File_Handling(Name_Of_File1,Name_Of_File2):

    ret1 = os.path.exists(Name_Of_File1)
    ret2 = os.path.exists(Name_Of_File2)

    if ret1 == True:
        print(f"{Name_Of_File1} does  exists.")

        if ret2 == True:
            print(f"{Name_Of_File2} does  exists.")

            fobj1 = open(Name_Of_File1,'r')

            data1 = fobj1.read()
            #print(data1)

            fobj2 = open(Name_Of_File2,'w+')

            fobj2.write(data1)
            fobj2.seek(0)#after write mode,cursor goes to the end,so to brinf it back this line
            # is used...and its very very important.

            data2 = fobj2.read()
            #print(data2)

            if data1 == data2:
                print(f"The data from source file {Name_Of_File1}is successfully copied to destination file {Name_Of_File2}")
            else:
                print("Data could not be copied.")
        else:
            print(f"{Name_Of_File1} does not exists.")
    else:
        print(f"{Name_Of_File2} does not exists.")


def main():
    print("Enter the name of source file: ")
    Fname1 = input()

    print("Enter the name of destination file: ")
    Fname2 = input()

    File_Handling(Fname1,Fname2)



if __name__ == "__main__":
    main()