import os

def Display(FileName):

    fobj = open(FileName,'r')

    data = fobj.read()

    return data
   
def main():
    print("Enter the file name: ")
    FName = input()

    ret1 = os.path.exists(FName)

    if ret1 == True:
        pass
    else:
        print(f"{FName} does not exists.Enter the correct file")
        return -1
    

    ret = Display(FName)

    print("The content in the file is: \n",ret)

if __name__ == "__main__":
    main()