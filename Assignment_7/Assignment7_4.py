from functools import reduce

Products = lambda no1,no2:no1 * no2

def main():
    NumList1 = []
    print("How many values do you want to enter: ")
    value1 = int(input())

    print("Enter the values: ")
    for i in range(1,value1+1):
        print(f"Enter number {i} of {value1}")
        value2 = int(input())
        NumList1.append(value2)

    NumList2  = reduce(Products,NumList1)

    print(f"The product of numbers is {NumList2}")

if __name__ == "__main__":
    main()