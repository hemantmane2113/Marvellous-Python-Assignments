from Arithmetic import *

def main():

    print("Enter the first number: ")
    Value1 = int(input())

    print("Enter the second number: ")
    Value2 = int(input())

    Addition = Add(Value1,Value2)
    Subtraction = Sub(Value1,Value2)
    Multiplication = Mult(Value1,Value2)
    Division = Div(Value1,Value2)

    print("The Addition is: ",Addition)
    print("The Subtraction is: ",Subtraction)
    print("The Multiplication is: ",Multiplication)
    print("The Division is: ",Division)


if __name__ == "__main__":
    main()