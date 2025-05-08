def Add(no1,no2):
    Addition = no1 + no2
    return Addition

def main():
    print("Enter first number: ")
    num1 = int(input())
    print("Enter second number: ")
    num2 = int(input())

    Value = Add(num1,num2)
    print("Output:",Value)

if __name__ == "__main__":
    main()