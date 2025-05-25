def Num(no):
    List = []
    cnt = 1
    Sum = 0
    while(cnt <= no):
        if(cnt % 2 != 0):
            pass
        else:
            List.append(cnt)

        cnt = cnt + 1
        
    for i in List:
        Sum = Sum + i 

    return Sum


def main():

    print("Enter the upto which you need a list of Even numbers")
    value = int(input())

    ret = Num(value)

    print(f"The  addition of even numbers from 1 to {value} is {ret}")
    

if __name__ == "__main__":
    main()