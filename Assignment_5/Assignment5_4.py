def Largest(No1,No2,No3):

    if No1 > No2 and No1 > No3:
        MaxNum = No1
    elif No2 > No3 and No2 > No1:
        MaxNum = No2
    else:
        MaxNum = No3

    return MaxNum

def main():
    print("Enter first number: ")
    value1 = int(input())

    print("Enter second number: ")
    value2 = int(input())

    print("Enter third number: ")
    value3 = int(input())

    ret = Largest(value1,value2,value3)
    print(f"The maximum number is {ret}")


if __name__ == "__main__":
    main()