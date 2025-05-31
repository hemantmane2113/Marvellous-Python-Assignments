iCount = 1
def Pattern(iNo):
    global iCount
    if(iCount <= iNo):
        print(iCount * " * ")
        iCount = iCount + 1
        Pattern(iNo)

def main():
    print("Enter the number.")
    iValue = int(input())

    Pattern(iValue)

if __name__ == "__main__":
    main()