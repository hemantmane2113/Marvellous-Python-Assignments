class Employee:

    def __init__(self,A,B,C):
        self.name = A
        self._department = B
        self.__salary = C

    def Display(self):
        print(f"The name of employee is {self.name}.")
        print(f"The department of employee is {self._department}")
        print(f"The salary of employee is {self.__salary}")
         
        
def main():
    obj = Employee("Hemant","R & D",50000)

    obj.Diplay()#everything is accessible inside the class
    print(obj.name)#outside the class but still accessible as it is public
    print(obj._department)#outside the class but still accessible but not receommned as it is protected
    print(obj.__salary)# outside the class so not accessible as it is private
    ## private can still be accessed outside the class syntax: obj.classname__attribute
    ## print(obj.Employee.__salary)

if __name__ == "__main__":
    main()