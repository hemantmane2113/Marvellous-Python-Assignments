class Numbers:

    def __init__(self,A):
        self.value = A

    def ChkPrime(self):
        for num in range(2,self.value):
                if self.value % num == 0:
                    return False
        else:
            return True 

    def ChkPerfect(self):
        Sum = 0
        for num in range(1,self.value):
            if self.value % num == 0:
                Sum = Sum + num

        if self.value == Sum:
            return True
        else:
            return False

    def Factors(self):
        FactList = []
        for num in range(1,self.value+1//2):
            if self.value % num == 0:
                FactList.append(num)
        
        return FactList


    def SumFactors(self):
        Sum = 0
        for num in range(1,self.value+1//2):
            if self.value % num == 0:
                Sum = Sum + num

        return Sum


    def __del__(self):
        pass
            

def main():
    
    print("Enter the number: ")
    iNo = int(input())

    obj1 = Numbers(iNo)
    obj2 = Numbers(iNo)
    obj3 = Numbers(iNo)
    obj4 = Numbers(iNo)

    ret1 = obj1.ChkPrime()
    if ret1 == True:
        print(f"{iNo} is a Prime Number.")
    else:
        print(f"{iNo} is not a Prime Number.")

    ret2 = obj2.ChkPerfect()
    if ret2 == True:
        print(f"{iNo} is Perfect Number.")
    else:
        print(f"{iNo} is not a Perfect Number.")

    ret3 = obj3.Factors()
    print(f"The factors of {iNo} are {ret3}.")

    ret4 = obj4.SumFactors()
    print(f"The sum of factors of {iNo} is {ret4}.")

    
    del obj1
    del obj2
    del obj3
    del obj4


if __name__ == "__main__":
    main()