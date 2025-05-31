class BookStore:
    NoOfBooks = 0
    def __init__(self,A,B):
        self.Name = A
        self.Author = B

        BookStore.NoOfBooks = BookStore.NoOfBooks + 1
        # self.BookNum = BookStore.NoOfBooks
        

    def Display(self):
        
        print("Name of book is : ",self.Name)
        print(f"The author for {self.Name} is {self.Author}")
        print(f"This is Book number {BookStore.NoOfBooks}")#self.BookNum

    def __del__(self):
        pass

def main():
    Obj1 = BookStore("Linux System Programming", "Robert Love")
    Obj1.Display()

    Obj2 = BookStore("C Programming", "Denis Ritchie")
    Obj2.Display()

    del Obj1
    del Obj2

if __name__ == "__main__":
    main()