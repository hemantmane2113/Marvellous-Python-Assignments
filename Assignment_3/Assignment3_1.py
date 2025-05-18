# Write a program which accept N numbers from user and store it into list.Return addition 
#of all elements from that list

def Addition_Of_List(nos):
    Add = 0
    for i in nos:
        Add = Add + i 

    return Add

def main():
    print("Enter how many numbers you want in a list")
    no = int(input())

    Alist = []

    for i in range(no):
        print("Enter the numbers: ")
        digit = int(input())
        Alist.append(digit)
       
    print(Alist)

    ret = Addition_Of_List(Alist)

    print("The addition of given numbers is:",ret)

if __name__ == "__main__":
    main()