Square = lambda no: no * no

Cube = lambda no: no * no * no



def main():

    print("Enter the number")
    value = int(input())

    ret1 = Square(value)
    ret2 = Cube(value)

    print(f"The square of {value} is {ret1}")
    print(f"The cube of {value} is {ret2}")

if __name__ == "__main__":
    main()
