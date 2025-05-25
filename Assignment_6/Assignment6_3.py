def Table(no):
    for i in range(1,11):
        print(f"{no} * {i} =",no * i )
        

def main():
    print("Enter the number of which you need a multiplication table")
    value = int(input())

    Table(value)


if __name__ == "__main__":
    main()