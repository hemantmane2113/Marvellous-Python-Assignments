iSum = 0

def SumOfN(iNo):
    global iSum
    if iNo > 0:
        iSum = iSum + iNo
        iNo = iNo - 1
        SumOfN(iNo)

    return iSum

def main():
    print("Enter the number.")
    iValue = int(input())

    iRet = SumOfN(iValue)

    print(f"The sum for 1 to {iValue} is {iRet}.")

if __name__ == "__main__":
    main()