import time
import threading


def Addition(iNo):
    iSum = 0
    for i in range(1,iNo+1):
        iSum = iSum + i 
    print(f"The total sum of numbers from 1 to {iNo} is {iSum}.")

def main():
    Start_time = time.time()
    print("Enter number upto which you want sum of: ")
    iValue = int(input())

    Thread1 = threading.Thread(target = Addition,args = (iValue,))

    Thread1.start()
    Thread1.join()


    End_time = time.time()

    Total_time = End_time  - Start_time

    print(f"Total time for execution is { Total_time}")


if __name__ == "__main__":
    main()