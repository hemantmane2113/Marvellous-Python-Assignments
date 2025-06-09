class Calculator:

    def __init__(self,A,B):
        self.number1 = A
        self.number2 = B 
        self.Addition = 0
        self.Substraction = 0
        self.Multiplication = 1
        self.Division = 1

    def Add(self):
        self.Addition = self.number1 + self.number2
        return self.Addition

    def Sub(self):
        self.Substraction = self.number1 - self.number2
        return self.Substraction

    def Mult(self):
        self.Multiplication = self.number1 * self.number2
        return self.Multiplication

    def Div(self):
        self.Division = self.number1 / self.number2
        return self.Division

    def __del__(self):
        pass

def main():

    print("Enter first number: ")
    iValue1 = int(input())

    while True:
        print("Enter second number: ")
        iValue2 = int(input())

        if iValue2 != 0:
            break
        else:
            print("Invalid Input.Enter the second number again: ")
        

    obj = Calculator(iValue1,iValue2)

    ret = obj.Add()
    print("Addition is: ",ret)

    ret = obj.Sub()
    print("Subtraction is: ",ret)

    ret = obj.Mult()
    print("Multiplication is: ",ret)

    ret = obj.Div()
    print("Division is: ",ret)

    del obj

if __name__ == "__main__":
    main()


