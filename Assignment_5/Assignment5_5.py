def OddEven(No):

    if No % 2 == 0:
        return True
    else:
        return False

def main():
    print("Enter number: ")
    value = int(input())

    ret = False
    ret = OddEven(value)

    if ret == True:
        print(f"The {value} is even.")
    else:
        print(f"The {value} is odd.")
        
  
if __name__ == "__main__":
    main()