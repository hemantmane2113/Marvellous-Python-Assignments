def Star(no):
    bristar = "* " * no
    return bristar

def main():
    print("Enter the number: ")
    value = int(input())
    number = Star(value)
    print(number)

if __name__ == "__main__":
    main()