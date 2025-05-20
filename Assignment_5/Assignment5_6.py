def CelToFah(temp):

    Fahrenheit = (temp * 9/5) + 32

    return Fahrenheit


def main():
    print("Enter the temperature in degree celcius: ")
    value = int(input())

    ret = CelToFah(value)
    print(f"The temperature in fahrenheit is {ret} F")


if __name__ == "__main__":
    main()