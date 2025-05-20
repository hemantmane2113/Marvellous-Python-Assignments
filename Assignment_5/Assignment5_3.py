def VotEligChk(value):

    if value < 0:
        print("Ivalid age.")
    elif  0 <= value < 18:
        print("Ineligible to vote.")
    else:
        print("Eligible to vote")
        
def main():
    print("Enter your age: ")
    age= int(input())

    VotEligChk(age)

if __name__ == "__main__":
    main()