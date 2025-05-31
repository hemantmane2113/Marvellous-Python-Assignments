iSum = 0
def DigitSum(iNo):
    global iSum
    if iNo > 0:
        d = iNo % 10
        iSum = iSum + d
        iNo = iNo // 10
        DigitSum(iNo)
        
    return iSum

def main():
    print("Enter the number.")
    iValue = int(input())

    iRet = DigitSum(iValue)

    print(f"The sum of digits of {iValue} is {iRet}.")

if __name__ == "__main__":
    main()