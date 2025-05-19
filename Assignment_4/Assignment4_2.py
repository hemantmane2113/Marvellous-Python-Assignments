Multiplication = lambda A,B : A * B


def main():
    print("Enter first number: ")
    no1 = int(input())

    print("Enter second number: ")
    no2 = int(input())

    ret = Multiplication(no1,no2)

    print(f"The multiplication of {no1} and {no2} is { ret}.")


if __name__ == "__main__":
    main()