from  functools import reduce

Even = lambda A: A % 2 == 0

Square = lambda A: A ** 2

Addition = lambda A,B: A + B 


def main():
    print("Enter the number of elements you want in a list: ")
    iNum = int(input())

    print("Enter the numbers: ")
    InputList = []
    for i in range(1,iNum+1):
        print(f"Enter {i} of {iNum}: ")
        iValue = int(input())
        InputList.append(iValue)

    print(InputList)

    FilterList = list(filter(Even,InputList))

    MapList = list(map(Square,FilterList))

    try:# way no 2 to handle the situation where no value passes through the filter
        ReduceList = reduce(Addition,MapList)
        print(ReduceList)
    except TypeError:
        print("No values to pass through the filter.")


if __name__ == "__main__":
    main()






