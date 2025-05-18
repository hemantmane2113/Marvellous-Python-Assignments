# Write a program which accept one number from user and check whether number is prime or not 

def FactorAddition(no):
    
    
    for i in range(2,no//2+1):
        if no % i == 0:
            return False
            break

    return True


def main():
    ret = False
    print("Enter the number: ")
    value = int(input())


    ret = FactorAddition(value)

    if(ret == True):
        print(f"The number {value} is prime.")
    else:
        print(f"The number {value} is  not prime.")


if __name__ == "__main__":
    main()