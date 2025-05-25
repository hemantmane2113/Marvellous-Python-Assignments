def ChkPrime(no):
    if no <= 1:
        print(f"{no} is neither prime nor composite")# Along with this line,code at line no 24 
        #also gets executed,if 0 and 1 is entered
        return None
        
    for i in range(2,no+1):
        if no % i == 0:
            return False
    
    return True

def main():
    
    print("Enter the number: ")
    value = int(input())

    ret = False

    ret = ChkPrime(value)

    if ret == True:
        print(f"{value} is prime")
    else:
        print(f"{value} is NOT prime")##  


if __name__ == "__main__":
    main()

