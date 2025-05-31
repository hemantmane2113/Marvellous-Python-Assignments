from  functools import reduce


LessthanEqualto = lambda A: 90 >= A >= 70

AddBy = lambda A: A + 10

Multiplication = lambda A,B: A * B 


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

    FilterList = list(filter(LessthanEqualto,InputList))

    if not FilterList:
        print("The given list cannot be filtered as no number meets the filter condition.Re-enter values.")
        return # way no 1 to handle the situation where no value passes through the filter
    
    MapList = list(map(AddBy,FilterList))

    ReduceList = reduce(Multiplication,MapList)

    print(ReduceList)


if __name__ == "__main__":
    main()






