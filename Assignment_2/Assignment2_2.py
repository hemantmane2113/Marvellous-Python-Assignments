# Write a program which accept one number and display below pattern

def Pattern(no):

    for i in range(no):
        print(no * " * ")


def main():

    print("Enter the number: ")
    value = int(input())

    ret = Pattern(value)


if __name__ == "__main__":
    main()