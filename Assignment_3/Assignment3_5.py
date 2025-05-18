from MarvellousNum import ChkPrime


def Addition_Of_Prime(nos):
    Add = 0
    for i in nos:
        Add = Add + i 

    return Add

def main():
    print("Enter how many numbers you want in a list")
    no = int(input())

    Alist = []

    for i in range(1,no+1):
        print(f"Enter the number {i} of {no}: ")
        digit = int(input())
        Alist.append(digit)
       
    #print(Alist)

    RetPrime = ChkPrime(Alist)

    
    print(RetPrime)
    

    RetAddition = Addition_Of_Prime(RetPrime)

    print("The addition of given numbers is:",RetAddition)

if __name__ == "__main__":
    main()