class Vehicle:

    def start(self):
        print(f"In class {__class__.__name__}")

class Car(Vehicle):

    def start(self):
        print(f"In child class {__class__.__name__}.")

def main():

    obj1 = Vehicle()
    obj2 = Car()

    obj1.start()
    obj2.start()


if __name__ == "__main__":
    main()