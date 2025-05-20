
Sum = lambda A,B:A + B

Difference = lambda A,B:A - B

Product = lambda A,B:A * B

Division = lambda A,B:A / B


def main():
    print("Enter first number.:")
    Value1 = int(input())

    print("Enter first number.:")
    Value2 = int(input())

    ret1 = Sum(Value1,Value2)
    print(f"Sum of {Value1} and {Value2} is {ret1}")

    ret1 = Difference(Value1,Value2)
    print(f"Diference of {Value1} and {Value2} is {ret1}")

    ret1 = Product(Value1,Value2)
    print(f"Product of {Value1} and {Value2} is {ret1}")

    ret1 = Division(Value1,Value2)
    print(f"Division of {Value1} and {Value2} is {ret1}")


if __name__ == "__main__":
    main()

