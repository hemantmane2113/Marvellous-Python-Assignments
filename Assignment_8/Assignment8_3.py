import threading

def EvenAddition(iNo):
    EvenSum = 0
    for i in iNo:
        if i % 2 == 0:
            EvenSum = EvenSum + i

    print(EvenSum)

def OddAddition(iNo):
    OddSum = 0
    for i in iNo:
        if i % 2 == 1:
            OddSum = OddSum + i

    print(OddSum)


def main():

    print("Enter the number of elements you want: ")
    iValue = int(input())

    print("Enter the  numbers: ")

    EvenOddList = []
    for i in range(1,iValue+1):
        print(f"Enter {i} of {iValue}: ")
        no = int(input())
        EvenOddList.append(no)
    
    print(EvenOddList)

    
    EvenList = threading.Thread(target = EvenAddition ,args = (EvenOddList,))
    OddList = threading.Thread(target = OddAddition ,args = (EvenOddList,))

    EvenList.start()
    OddList.start()

    EvenList.join()
    OddList.join()


if __name__ == "__main__":
    main()