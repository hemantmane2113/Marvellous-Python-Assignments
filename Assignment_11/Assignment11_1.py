Result = []
def PrintNum(iNo):
    global Result
    
    if(iNo > 0):
        Result.append(iNo)
        iNo = iNo - 1
        PrintNum(iNo)

    return Result

def main():
    print("Enter the number: ")
    iValue = int(input())

    iRet = PrintNum(iValue)
    iRet.reverse()

    print(f"The numbers are {iRet}.")


if __name__ == "__main__":
    main()