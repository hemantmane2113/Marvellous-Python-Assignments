class Demo:
    Value = "class_variable"

    def __init__(self,A,B):
        print("Inside Constructor")
        self.No1 = A
        self.No2 = B 

    def Fun(self):
        print(self.No1,self.No2)

    def Gun(self):
        print(self.No1,self.No2)

    def __del__(self):
        print("Inside Destructor")


def main():


    obj1 = Demo(11,21)
    obj2 = Demo(51,101)


    ret = obj1.Fun()
    

    ret = obj2.Fun()
    

    ret = obj1.Gun()
    

    ret = obj2.Gun()


    del obj1
    del obj2


if __name__ == "__main__":
    main()