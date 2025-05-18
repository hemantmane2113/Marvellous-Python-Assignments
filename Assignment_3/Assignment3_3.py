# Write a program which accept N numbers from user and store it into list.Return minimumS 
#number from that list

def Minimum_Of_List(nos):
    Min = nos[0]
    for i in nos:
        if Min >= i:
            Min = i
            

    return Min

def main():
    print("Enter how many numbers you want in a list")
    no = int(input())

    Alist = []

    for i in range(no):
        print("Enter the numbers: ")
        digit = int(input())
        Alist.append(digit)
       
    print(Alist)

    ret = Minimum_Of_List(Alist)

    print("The minimum of given numbers is:",ret)

if __name__ == "__main__":
    main()
