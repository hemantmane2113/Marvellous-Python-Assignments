class Student:
    school_name = 'kendriya vidyalaya'

    def __init__(self,A,B):
        self.name = A
        self.roll_number = B

    def Display(self):
        print("The name of student is ",self.name)
        print("The roll number of student is ",self.roll_number)
        print("The current school name is ",Student.school_name)

    def Change(self):
        Student.school_name = "Navoday Vidhyalaya"

        print("The new school name is ",Student.school_name)

    def __del__(self):
        pass


def main():
    obj = Student('Hemant',3121)
    obj.Display()
    obj.Change()

    del obj


if __name__ == "__main__":
    main()
