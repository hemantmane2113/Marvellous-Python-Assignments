def ChkPrime(No1):
    LenOfNo1 = len(No1)
    for i in (No1):
        for j in range(2,i):
            if i % j == 0:
                break
        else:
            Prime.append(True)   
        
    return Prime

A = [3,6,7,9,11]
ret = ChkPrime(A)
print(ret)




