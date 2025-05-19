from functools import reduce

Even = lambda No1:(No1 % 2 == 0)

Square = lambda No2:(No2 * No2)

Addition = lambda No3,No4:(No3 + No4)


def main():
    print("Enter how many numbers you want to enter in the list")
    NumCnt = int(input())
    ValList1 = []
    for i in range(1,NumCnt+1):
        print(f"Enter value no {i}:")

        num = int(input())

        ValList1.append(num)

    ValList2 = list(filter(Even,ValList1))
    print("The filtered list is :",ValList2)

    ValList3 = list(map(Square,ValList2))
    print(f"The list after addition of 10 becomes: ",ValList3)

    Value = reduce(Addition,ValList3)
    print("The value of reduced list is: ",Value)


if __name__ == "__main__":
    main()