class Circle:
    PI = 3.14

    def __init__(self):
        self.Radius = 0.0
        self.Area = 0.0
        self.Circumference = 0.0

    def Accept(self):

        print("Enter the radius:")
        self.Radius = float(input())

    def CalculateArea(self):
    
        self.Area = Circle.PI * self.Radius ** 2
        

    def CalculateCircumference(self):
        
        self.Circumference = 2 * Circle.PI * self.Radius
        

    def Display(self):

        print("Radius of circle: ",self.Radius)
        
        print("Circumference of circle: ",self.Circumference)

        print("Area of circle: ",self.Area)
        

    def __del__(self):
        pass

def main():
    
    obj = Circle()
    
    
    obj.Accept()
    obj.CalculateArea()
    obj.CalculateCircumference()
    obj.Display()
    

    del obj
   

if __name__ == "__main__":
    main()