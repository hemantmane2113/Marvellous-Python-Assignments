def ConVowChk(char):
    vowel = ['a','e','i','o','u']

    if char in vowel:
        return True
    else:
        return False

def main():

    
    print("Enter the character: ")
    value1 = input()


    if len(value1) > 1:# to check whether the length of string is exactly 1
        print("Invalid character")
        return
    
    if value1.isdigit():# to check whether its a number or not
        print("Invalid character")
        return
   
    value2 = value1.lower()

    ret = False

    ret = ConVowChk(value2)

    if ret == True:
        print(f"{value1} is vowel.")

    else:
        print(f"{value1} is consonant.")


if __name__ == "__main__":
    main()