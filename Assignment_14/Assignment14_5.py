class BankAccount:

    def __init__(self,A,B,C):
        self.Account_Number = A
        self.Name = B 
        self.Balance = C 
        

    def Deposit(self):
        print("Enter the amount to deposit: ")
        Amount = int(input())
        self.Balance = self.Balance + Amount

    def WithDraw(self):
        print("Enter the amount to WithDraw: ")
        Amount = int(input())
        self.Balance = self.Balance - Amount

    def Display(self):
        print("Name of customer is: ",self.Name)
        print("Account Number of Customer is: ",self.Account_Number)
        print("Current Balance is : ",self.Balance)

    def __del__(self):
        pass

    
def main():
    Obj1 = BankAccount(30903753659,'Hemant',2700)
    Obj1.Deposit()
    Obj1.WithDraw()
    Obj1.Display()

    del Obj1

if __name__ == "__main__":
    main()


    