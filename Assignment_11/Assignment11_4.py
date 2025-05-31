iPower = 1
def Power(iNo1,iNo2):
    global iPower
    if iNo2 > 0:
        iPower = iPower * iNo1
        iNo2 = iNo2 - 1
        Power(iNo1,iNo2)

    return iPower

def main():
    print("Enter the number.")
    iValue1 = int(input())

    print("Enter the power.")
    iValue2 = int(input())

    iRet = Power(iValue1,iValue2)

    print(f"{iValue1} power {iValue2} is {iRet}.")

if __name__ == "__main__":
    main()