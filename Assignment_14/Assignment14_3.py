class Book:

    def __init__(self,A):
        self.__price = A

    def get_price(self):
        print("The current price of book is: ",self.__price)

    def set_price(self):
        print("Enter the amount by how much do you want to increase the price of book: ")
        Amount = int(input())
        self.__price = self.__price + Amount

    def Display(self):
        print("New price of book is: ",self.__price)

    def __del__(self):
        pass



def main():

    obj = Book(50)
    obj.get_price()
    obj.set_price()
    obj.Display()

    del obj


if __name__ == "__main__":
    main()