def RetPrime(no):
    if no <= 1:
        return False:

    for i in range(2,no):
        if no % i == 0:
            return False
    else:
        return True


def main():
    NumList1 = []

    print("Enter how many numbers you want in a list: ")
    value1 = int(input())

    for i in range(1,value1+1):
        print(f"Enter number {i} of {value1} and press enter.")
        value2 = int(input())
        NumList1.append(value2)

    NumList2 = list(filter(RetPrime,NumList1))

    print(f"The prime numbers are {NumList2}.")



if __name__ == "__main__":
    main()