def ChkNum(value):
    if value % 2 == 0:
        print("Even number")
    else:
        print("Odd number")

def main():
    print("Enter the number: ")
    no = int(input()) 
    number = ChkNum(no)


if __name__ == "__main__":
    main()