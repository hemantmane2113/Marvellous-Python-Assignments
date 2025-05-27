import time

def Addition(iNo):
    iSum = 0
    for i in range(1,iNo+1):
        iSum = iSum + i 
    return iSum

def main():
    Start_time = time.time()
    print("Enter number upto which you want sum of: ")
    iValue = int(input())

    iRet = Addition(iValue)

    print(f"The sum of numbers from 1 to {iValue} is {iRet}.")

    End_time = time.time()

    Total_time = End_time  - Start_time

    print(f"Total time for execution is { Total_time}")


if __name__ == "__main__":
    main()