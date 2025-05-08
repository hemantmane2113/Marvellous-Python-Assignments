def LenSize(char):
    charlen = len(char)
    return charlen

def main():
    print("Enter the word: ")
    word = input()

    length = LenSize(word)
    print(length)

if __name__ == "__main__":
    main()