def Num(no):
    List = []
    cnt = 1
    while(cnt <= no):
        List.append(cnt)
        cnt = cnt + 1
    return List


def main():

    print("Enter the upto which you need a list of  numbers")
    value = int(input())

    ret = Num(value)
    print(f"The  numbers from 1 to {value} is {ret}")
    

if __name__ == "__main__":
    main()