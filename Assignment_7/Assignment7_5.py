def Palindrome(char):
    if char[0::]==char[::-1]:
        return True 
    else: 
        return False


def main():
    print("Enter the string: ")
    strg = input()
    strgg = strg.lower()

    ret = False
    ret = Palindrome(strg)

    if ret == True:
        print(f"{strg} is palindrome.")
    else:
        print(f"{strg} is not a palindrome.")


if __name__ == "__main__":
    main()