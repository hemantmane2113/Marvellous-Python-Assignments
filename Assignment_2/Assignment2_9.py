# Write a prog which accept number from user and return number of digits in that number

def Digits(no):
    counter = 0
    #Digits = []
    while(no > 0):
        Digit = no % 10
        #Digits.append(Digit)
        counter = counter + 1
        no = no//10
    
    return counter

def main():

    value = 0
    ret = 0
    print("Enter the number: ")
    value = int(input())

    ret = Digits(value)
    print("The total number of digits are:",ret)

if __name__ == "__main__":
    main()