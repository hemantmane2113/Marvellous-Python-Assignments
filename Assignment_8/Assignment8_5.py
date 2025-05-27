import threading

def DisplayStraight(iNo):
    Straight = []
    for i in range(1,iNo+1):
        Straight.append(i)

    print(Straight)

def DisplayReverse(iNo):
    Reverse = []
    for i in range(iNo,0,-1):
        Reverse.append(i)

    print(Reverse)


def main():

    print("Enter the number: ")
    iValue = int(input())

    
    Thread1 = threading.Thread(target = DisplayStraight ,args = (iValue,))
    Thread2 = threading.Thread(target = DisplayReverse ,args = (iValue,))

    Thread1.start()
    Thread1.join()

    Thread2.start()
    Thread2.join()


if __name__ == "__main__":
    main()