# Write a program which accept number from user and return addition of digits in that number

def Digits(no):
    Sum = 0
    #Digits = []
    while(no > 0):
        Digit = no % 10
        #Digits.append(Digit)
        Sum = Sum + Digit
        no = no//10
    
    return Sum

def main():

    value = 0
    ret = 0
    print("Enter the number: ")
    value = int(input())

    ret = Digits(value)
    print("The total addition of digits are:",ret)

if __name__ == "__main__":
    main()