Power = lambda A:A**2

def main():
    print("Enter the number: ")
    iValue = int(input())

    iRet = Power(iValue)

    print(f"The Square of {iValue} is {iRet}.")

if __name__ == "__main__":
    main()