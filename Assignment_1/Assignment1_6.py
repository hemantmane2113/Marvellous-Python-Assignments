def PosNeg(no):
    if no > 0:
        return "Number is positive"
    elif no < 0:
        return "Number is Negative"
    else:
        return "Number is Zero"

def main():
    print("Enter the number: ")
    value = int(input())

    number = PosNeg(value)
    print(number)

if __name__ == "__main__":
    main()