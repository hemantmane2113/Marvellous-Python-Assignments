iFact = 1
def Factorial(iNo):
    global iFact
    
    if(iNo > 0):
        iFact = iNo * iFact
        iNo = iNo - 1
        Factorial(iNo)

    return iFact

def main():
    print("Enter the number: ")

    iValue = int(input())

    if iValue == 0:
        print("The Factorial of 0 is 1.")
        return None
        
    if iValue < 0:
        print("The Factorial of negative number does not exist.")
        return None
        
    if iValue > 0:
        iRet = Factorial(iValue)
          

    print(f"The Factorial of {iValue} is {iRet}.")


if __name__ == "__main__":
    main()