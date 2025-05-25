def ChkPrime(no):
    if no <= 1:
        return None
        # improvement over Assignment6_5c.py

    for i in range(2,no):
        if no % i == 0:
            return False
    
    return True

def main():
    
    print("Enter the number: ")
    value = int(input())

    ret = False

    ret = ChkPrime(value)

    if ret == None:
        print(f"{value} is neither prime nor composite.")
        return## this return is also very important

    if ret == True:
        print(f"{value} is prime")
    else:
        print(f"{value} is NOT prime")


if __name__ == "__main__":
    main()