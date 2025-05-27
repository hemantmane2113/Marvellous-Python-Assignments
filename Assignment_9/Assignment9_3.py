import multiprocessing
import os

def Factorial(iNo):
    
    Factorial = 1
    for i in range(1,iNo+1):
        Factorial = Factorial * i
    
    return Factorial

    
def main():
    

    print("Enter the number of elements you want in list: ")
    iValue = int(input())

    print("Enter the numbers in a list: ")
    NumList = []
    for i in range(1,iValue+1):
        print(f"Enter number {i} of {iValue}")
        iNum = int(input())
        NumList.append(iNum)

    print(f"The numbers entered are {NumList}")

    p = multiprocessing.Pool()
    

    Result = list(p.map(Factorial,NumList))

    p.close()
    p.join()

    print(Result)
    


if __name__ == "__main__":
    main()