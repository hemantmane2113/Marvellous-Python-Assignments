iCount = 0

def CountZero(iNo):
    global iCount

    if iNo  > 0:
        digit = iNo % 10
        iNo = iNo // 10
        if digit == 0:
            iCount = iCount + 1
        CountZero(iNo)

    return iCount

def main():
    print("Enter the number.")
    iValue = int(input())

    iRet = CountZero(iValue)

    print(f"The total number of zeros in  {iValue} is {iRet}.")

if __name__ == "__main__":
    main()