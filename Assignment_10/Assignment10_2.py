Multiplication = lambda A,B:A * B

def main():
    print("Enter the first number: ")
    iValue1 = int(input())

    print("Enter the second number: ")
    iValue2 = int(input())

    iRet = Multiplication(iValue1,iValue2)

    print(f"The multiplication of {iValue1} and {iValue2} is {iRet}.")

if __name__ == "__main__":
    main()