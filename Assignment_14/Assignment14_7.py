class Person:

    def __init__(self,A,B):
        self.Name = A
        self.Age = B 


class Teacher(Person):
    
    def __init__(self,C,D,E,F):# initial attributes for parent class and later for child class
        self.Subject = E
        self.Salary = F
        super().__init__(C,D) # behind the scenes:Person.__init__(self,C,D)where C = A and D = B

        print("Name is ",self.Name)
        print("Age is ", self.Age)
        print("Subject is ",self.Subject)
        print("Salary is  ",self.Salary)

   


def main():

    obj = Teacher("Hemant",34,"Data Science",40000)


if __name__ == "__main__":
    main()




