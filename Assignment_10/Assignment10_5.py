from  functools import reduce


def Prime(A):
    for i in range(2,A):
        if(A % i == 0):
            return False
            break
    else:
        return True

MultiplyBy = lambda A: A * 2

Maximum = lambda A,B: max(A,B) 


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

    FilterList = list(filter(Prime,InputList))

    if not FilterList:
        print("The given list cannot be filtered as no number meets the filter condition.Re-enter values.")
    # way no 3 to handle the situation where no value passes through the filter
    
    MapList = list(map(MultiplyBy,FilterList))

    ReduceList = reduce(Maximum,MapList,0)# 0 if no value in reducelist
    # way no 3 to handle the situation where no value passes through the filter
    print(ReduceList)


if __name__ == "__main__":
    main()






