
Power = lambda a:a **2


def main():
    print("Enter the number:")
    iValue = int(input())

    ret = Power(iValue)

    print(f"The square of {iValue} is {ret}.")


if __name__ == "__main__":
    main()