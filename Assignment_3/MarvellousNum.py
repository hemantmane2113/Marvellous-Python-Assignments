def ChkPrime(no):
    PrimeList = []
    LenOfNo = len(no)
    for i in no:
        for j in range(2,LenOfNo):
            if i % j == 0:
                break
        else:
            PrimeList.append(i)
        
    return PrimeList