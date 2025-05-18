# Write a program which accept N numbers from user and store it into list.Return maximum 
#number from that list

def Maximum_Of_List(nos):
    Max = 0
    for i in nos:
        if Max < i:
            Max = i
            

    return Max

def main():
    print("Enter how many numbers you want in a list")
    no = int(input())

    Alist = []

    for i in range(no):
        print("Enter the numbers: ")
        digit = int(input())
        Alist.append(digit)
       
    print(Alist)

    ret = Maximum_Of_List(Alist)

    print("The maximum of given numbers is:",ret)

if __name__ == "__main__":
    main()