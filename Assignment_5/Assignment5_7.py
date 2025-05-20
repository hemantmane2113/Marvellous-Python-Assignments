def ArePeri(length,width):

    Area = length * width

    Perimeter = 2 * length + 2 * width

    return Area,Perimeter


def main():

    print("Enter length: ")
    value1 = float(input())

    print("Enter width: ")
    value2 = float(input())

    ret = ArePeri(value1,value2)

    print(f"The area of rectange is {ret[0]}")
    print(f"The area of rectange is {ret[1]}")

if __name__ == "__main__":
    main()


