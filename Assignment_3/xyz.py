def ChkPrime(num):    
    len_list = len(num)
    pl_list = []
    for i in num:
        for j in range(2, len_list):
            if i % j == 0:
                break
        else:
            pl_list.append(i)
            
    return pl_list
          
        


def main():
    value1 = [2,6,5,8,7]

    ret = ChkPrime(value1)

    print(ret)
    


if __name__ == "__main__":
    main()
