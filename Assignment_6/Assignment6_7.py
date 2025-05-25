def Maximum(nos):
    Maximum = nos[0]
    for i in range(len(nos)):
        if Maximum < nos[i]:
            Maximum = nos[i]

    return Maximum



def main():
    NumList = []

    print("Enter numbers: ")
   
    for i in range(1,6):
        print(f"print number {i} of 6 and Press Enter:")
        value = int(input())
        NumList.append(value)

    ret = Maximum(NumList)
    print(f"The maximum number is {ret}")

if __name__ == "__main__":
    main()