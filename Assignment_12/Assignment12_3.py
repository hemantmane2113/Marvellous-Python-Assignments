class Arithematic:

    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0

    def Accept(self):
        print("Enter first number:")
        self.Value1 = int(input())
        

        print("Enter second number: ")
        self.Value2 = int(input())

        return self.Value1,self.Value2

    def Addition(self):
        iAdd = self.Value1 + self.Value2
        return iAdd

    def Substraction(self):
        iSub = self.Value1 - self.Value2
        return iSub

    def Multiplication(self):
        iMulti = self.Value1 * self.Value2
        return iMulti

    def Division(self):
        iDiv = self.Value1 / self.Value2
        return iDiv

    

    def __del__(self):
        pass

    
def main():
    obj = Arithematic()

    ret = obj.Accept()
    print(f"The two values are {ret[0]} and {ret[1]}")
    print(f"The two values are {obj.Value1} and {obj.Value2}")# you can use this as well if
    # in case obj.Accept() is to be just called and not assigned to any variable.

    ret = obj.Addition()
    print(f"The addition is {ret}")

    ret = obj.Substraction()
    print(f"The substraction is {ret}")

    ret = obj.Multiplication()
    print(f"The multiplication is {ret}")

    ret = obj.Division()
    print(f"The division is {ret}")

    del obj
    

if __name__ == "__main__":
    main()