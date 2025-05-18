# Write a program which accept one number and return addition of its factors

def FactorAddition(no):
    
    Add = 0
    for i in range(1,no//2+1):
        if no % i == 0:
            Add = Add + i 

    return Add


def main():

    print("Enter the number: ")
    value = int(input())

    ret = FactorAddition(value)

    print(f"The addition of factors of {value} is:{ret}")


if __name__ == "__main__":
    main()