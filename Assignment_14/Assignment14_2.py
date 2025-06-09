class Rectangle:

    def __init__(self,A,B):
        self.Length = A
        self.Width = B

    def CalculateArea(self):
        self.Area = self.Length * self.Width

    def CalculatePerimeter(self):
        self.Perimeter = 2 * self.Length + 2 * self.Width

    def Display(self):
        print(f"The area of rectangle  is {self.Area} square units.")
        print(f"The perimeter of rectangle  is {self.Perimeter} units.")


def main():
    obj1 = Rectangle(10,5)
    obj1.CalculateArea()
    obj1.CalculatePerimeter()
    obj1.Display()


if __name__ == "__main__":
    main()   