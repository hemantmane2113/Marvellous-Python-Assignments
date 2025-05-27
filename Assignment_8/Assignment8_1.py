import threading


def DisplayEven(iNo):
    EvenList = []
    for i in range(iNo+1):
        if(i % 2 == 0):
            EvenList.append(i)

    print(EvenList)

def DisplayOdd(iNo+1):
    OddList = []
    for i in range(iNo):
        if(i % 2 == 1):
            OddList.append(i)

    print(OddList)


def main():

    print("Enter the number : ")
    iValue = int(input())

    Even = threading.Thread(target = DisplayEven,args = (iValue,))
    Odd = threading.Thread(target = DisplayOdd,args = (iValue,))


    Even.start()
    Odd.start()

    Even.join()
    Odd.join()


if __name__ == "__main__":
    main()