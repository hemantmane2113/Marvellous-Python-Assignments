import threading

def EvenFactorsAddition(iNo):
    EvenFactors = []
    Sum = 0
    for i in range(1,iNo+1):
        if((iNo % i == 0) & (i % 2 == 0)):
            EvenFactors.append(i)
        
    for j in EvenFactors:
         Sum = Sum + j

    print(Sum)

def OddFactorsAddition(iNo):
    OddFactors = []
    Sum = 0
    for i in range(1,iNo+1):
        if ((iNo % i == 0) & (i % 2 == 1)):
            OddFactors.append(i)
        
    for j in OddFactors:
        Sum = Sum + j

    print(Sum)


def main():

    print("Enter the number : ")
    iValue = int(input())
    
    EvenFactor = threading.Thread(target = EvenFactorsAddition,args = (iValue,))
    OddFactor = threading.Thread(target = OddFactorsAddition,args = (iValue,))

    EvenFactor.start()
    OddFactor.start()

    EvenFactor.join()
    OddFactor.join()

    print("exit from main")


if __name__ == "__main__":
    main()