import os


def File_Handling(List_Of_Numbers,Name_Of_File = "Numbers.txt"):

    fobj = open(Name_Of_File,'w+') # write + read

    ret = os.path.exists(Name_Of_File)

    if ret == True:
        print(f"File is successfully created by the name {Name_Of_File}")
    else:
        print("No such file exists.")

    counter = 1
    for number in List_Of_Numbers:
            fobj.write(str(counter) + ". " + str(number) + "\n")
            counter = counter + 1

    fobj.seek(0)## to bring back cursor to start if names are to be printed one after 
    #the other and not to the new line.
    data = fobj.read()

    if data == List_Of_Numbers:
        print(f"Data is successfully entered into the file {Name_Of_File}")

    fobj.close()

    
def main():

    print("Enter how many numbers you want to enter: ")
    iValue = int(input())

    NumList = []

    for i in range(1,iValue+1):
        print(f"Enter number {i}: ")
        no = input()
        NumList.append(no)

    File_Handling(NumList)


if __name__ == "__main__":
    main()