import multiprocessing
import os

def Square(iNo):
    SquareList = []
    for i in iNo:
        Square = i ** 2
        SquareList.append(Square)

    print(f"Child process  PID: {os.getpid()} -> Result: {SquareList}")

def main():
    print(f"Inside main ,PID: {os.getpid()}")

    print("Enter the number of elements you want in list: ")
    iValue = int(input())

    print("Enter the numbers in a list: ")
    NumList = []
    for i in range(1,iValue+1):
        print(f"Enter number {i} of {iValue}")
        iNum = int(input())
        NumList.append(iNum)

    print(f"The numbers entered are {NumList}")

    Process1 = multiprocessing.Process(target = Square,args = (NumList,))
    Process2 = multiprocessing.Process(target = Square,args = (NumList,))

    Process1.start()
    Process2.start()

    print(f"Process1 PID: {Process1.pid}")
    print(f"Process2 PID: {Process2.pid}")


    Process1.join()
    Process2.join()


if __name__ == "__main__":
    main()