from functools import reduce

GreatSmall = lambda no1 :(70 <= no1 <= 90)

Increase = lambda no2 :(no2 + 10)

Reduce = lambda no3,no4 : (no3 * no4)


def main():
    print("Enter how many numbers you want to enter in the list")
    NumCnt = int(input())
    ValList1 = []
    for i in range(1,NumCnt+1):
        print(f"Enter value no {i}:")

        num = int(input())

        ValList1.append(num)

    ValList2 = list(filter(GreatSmall,ValList1))
    print("The filtered list is :",ValList2)

    ValList3 = list(map(Increase,ValList2))
    print(f"The list after addition of 10 becomes: ",ValList3)

    Value = reduce(Reduce,ValList3)
    print("The value of reduced list is: ",Value)


if __name__ == "__main__":
    main()