def Triangle(rows,columns):
    for i in range(1,rows+1):
        for j in range(1,columns+1):
            if(i >= j):
                print(" * ",end = " ")
        print()       

def main():
    print("Enter number of rows")
    value1 = int(input())

    print("Enter number of columns")
    value2 = int(input())

    ret = Triangle(value1,value2)


if __name__ == "__main__":
    main()