import threading
import os

def CountSmall(x):
    SmallSum = 0
    for i in x:
        if i.islower():
            SmallSum = SmallSum + 1
    
    print(SmallSum)

    current_thread = threading.current_thread()#reference-chatgpt
    print("The PID of CountSmall thread is: ",os.getpid())
    print("The PPID of CountDigit thread is: ",os.getppid())
    print("Thread ID of child thread CountSmall is: ",threading.get_ident())
    print(f"Thread ID of {current_thread.name} is: {threading.get_ident()}")#reference-chatgpt
    

def CountCapital(x):
    CapitalSum = 0
    for i in x:
        if i.isupper():
            CapitalSum = CapitalSum + 1
    
    print(CapitalSum)

    current_thread = threading.current_thread()
    print("The PID of CountCapital thread is: ",os.getpid())
    print("The PPID of CountDigit thread is: ",os.getppid())
    print("Thread ID of child thread CapitalSum is: ",threading.get_ident())
    print(f"Thread ID of {current_thread.name} is: {threading.get_ident()}")


def CountDigit(x):
    DigitSum = 0
    for i in x:
        if i.isdigit():
            DigitSum = DigitSum + 1
    
    print(DigitSum)

    current_thread = threading.current_thread()
    print("The PID of CountDigit thread is: ",os.getpid())
    print("The PPID of CountDigit thread is: ",os.getppid())
    print("Thread ID of child thread CountDigit is: ",threading.get_ident())
    print(f"Thread ID of {current_thread.name} is: {threading.get_ident()}")



def main():

    print("Enter the number of elements you want: ")
    iValue = int(input())

    print("Enter the elements: ")

    AlphaNumeric = []
    for i in range(1,iValue+1):
        print(f"Enter {i} of {iValue}: ")
        no = input()
        AlphaNumeric.append(no)
    
    print(AlphaNumeric)

    current_thread = threading.current_thread()
    print("The PID of main thread is: ",os.getpid())
    print("The PPID of main thread is: ",os.getppid())
    print(f"Thread ID of {current_thread.name} is: {threading.get_ident()}")

    Small = threading.Thread(target = CountSmall,args = (AlphaNumeric,))
    Capital = threading.Thread(target = CountCapital,args = (AlphaNumeric,))
    Digit = threading.Thread(target = CountDigit,args = (AlphaNumeric,))


    Small.start()
    Capital.start()
    Digit.start()

    
    Small.join()
    Capital.join()
    Digit.join()


if __name__ == "__main__":
    main()

# PID will be same for all the threads including main thread
# PPID will be same for all the threads including main thread
# TID can be same/different for different child threads.Its totally different for main thread.
