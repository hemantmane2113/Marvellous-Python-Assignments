# Write a program which accept N numbers from user and store it into list.accept one another
#number from user and return frequency of that number from list.

def Freq_Of_Num(number,nos):
    Freq = 0
    
    for i in nos:
        if i == number:
            Freq = Freq + 1
            

    return Freq

def main():
    print("Enter how many numbers you want in a list")
    no = int(input())

    Alist = []

    for i in range(no):
        print("Enter the numbers: ")
        digit = int(input())
        Alist.append(digit)
       
    print(Alist)

    print("Enter digit of which you want to check frequency:")
    num = int(input())

    ret = Freq_Of_Num(num,Alist)

    print("The frequency of given numbers is:",ret)

if __name__ == "__main__":
    main()
