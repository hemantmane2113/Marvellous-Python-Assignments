# Syntax: def __eq__(self, other): return self.argument == other.argument

class Product:
    
    def __init__(self,A,B):
        self.name = A 
        self.price = B 

    def __eq__(self,other):
        #return self.name == other.name and self.price == other.price
        #return self.name == other.name or self.price == other.price
        #return self.name == other.name
        return self.price == other.price## returns only one value..so any one at any


def main():
    obj1 = Product("Jeans",2000)
    obj2 = Product("Shirt",1500)
    obj3 = Product("Jeans",2000)
    obj4 = Product("Shirt",2500)
    obj5 = Product("Shoes",1500)

    print(obj1 == obj2)
    print(obj1 == obj3)
    print(obj2 == obj4)
    print(obj2 == obj5)

if __name__ == "__main__":
    main()

