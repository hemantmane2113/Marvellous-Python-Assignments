# Write a program which accept one number and display below pattern

def Pattern(no):

    for i in range(no+1):
        for j in range(1,i+1):# range for this for loop is crucial
            print(j,end = " ")
        print()    
        

def main():

    print("Enter the number: ")
    value = int(input())

    ret = Pattern(value)


if __name__ == "__main__":
    main()