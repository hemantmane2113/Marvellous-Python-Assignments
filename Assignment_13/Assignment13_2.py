class BankAccount:
    ROI = 10.5

    def __init__(self):
        self.Name = "0"
        self.Amount = 0
        self.Time = 0

    def Deposit(self):
        print("Enter your Name: ")
        self.Name = input()

        print("Enter the amount: ")
        self.Amount = int(input())

        print("Enter the time period of keeping the amount in years: ")
        self.Time = int(input())

    def Withdraw(self):
        print("Enter the amount to be withdrawn: ")
        WAmount = int(input())

        WithAmount = self.Amount - WAmount
        self.WithdrawnAmount = WithAmount

    def CaculateInterest(self):
        Interest = (self.WithdrawnAmount * BankAccount.ROI * self.Time) / 100
        self.InterestEarned = Interest

    def Display(self):

        print("The name of Customer is : ",self.Name)
        print("The amount with the customer in is Rs: ",self.Amount)
        print("The amount remaining after the withdrawl by the customer is Rs: ",self.WithdrawnAmount)
        print(f"The  interest earned on {self.WithdrawnAmount } for the period {self.Time} years is Rs:{self.InterestEarned}")

    def __del__(self):
        pass

def main():

    Obj = BankAccount()

    Obj.Deposit()
    Obj.Withdraw()
    Obj.CaculateInterest()
    Obj.Display()

    del Obj


if __name__ == "__main__":
    main()