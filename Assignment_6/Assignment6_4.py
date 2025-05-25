def Fact(no):
    Fact = 1

    for i in range(1,no+1):
        Fact = Fact * i 

    return Fact

def main():

    print("Enter the number: ")
    value = int(input())

    if value < 0:
        print("Invalid number")
        return
        

    if value == 0:
        print("Factorial of 0 is 1.")
        return
        
    

    ret = Fact(value)

    print(f"Factorial of {value} is {ret}.")


if __name__ == "__main__":
    main()