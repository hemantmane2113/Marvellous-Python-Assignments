def Divby5(no):
    if no % 5 == 0:
        return True
    else:
        return False

def main():
    print("Enter the number: ")
    value = int(input())

    number = Divby5(value)
    print("Divisible by 5: ",number)

if __name__ == "__main__":
    main()