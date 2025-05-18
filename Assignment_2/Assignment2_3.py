# Write a program which accept one number and return its factorial

def Factorial(no):
    fact = 1
    for i in range(1,no+1):
        fact = fact * i 

    return fact


def main():

    print("Enter the number: ")
    value = int(input())

    ret = Factorial(value)

    print(f"The factorial of {value} is:{ret}")


if __name__ == "__main__":
    main()