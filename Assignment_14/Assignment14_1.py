class Employee:

    def __init__(self,A,B,C):
        self.name = A
        self.emp_id = B
        self.salary = C 

    def Display(self):
        print("The name of employee is: ",self.name)
        print("The employee_id of employee is: ",self.emp_id)
        print("The name of employee is: ",self.salary)

def main():
    obj1 = Employee('Rohit',101,50000)
    obj1.Display()

if __name__ == "__main__":
    main()