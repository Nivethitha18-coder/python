# Base Class
class Vehicle:
    def __init__(self):
        self.make = ""
        self.year = ""
        self.colour = ""

    def getdetails(self):
        self.make = input("Enter Vehicle Make: ")
        self.year = input("Enter Manufacturing Year: ")
        self.colour = input("Enter Vehicle Colour: ")

    def display_info(self):
        print("\n--- Vehicle Details ---")
        print("Make:", self.make)
        print("Year:", self.year)
        print("Colour:", self.colour)


# Derived Class - Car
class Car(Vehicle):
    def __init__(self):
        super().__init__()
        self.model = ""
        self.capacity = ""

    def getCardetails(self):
        self.model = input("Enter Car Model: ")
        self.capacity = input("Enter Seating Capacity: ")

    def display_car(self):
        print("\n--- Car Details ---")
        print("Model:", self.model)
        print("Capacity:", self.capacity)


# Derived Class - Bike
class Bike(Vehicle):
    def __init__(self):
        super().__init__()
        self.type = ""
        self.mileage = ""

    def getBikedetails(self):
        self.type = input("Enter Bike Type: ")
        self.mileage = input("Enter Mileage: ")

    def display_bike(self):
        print("\n--- Bike Details ---")
        print("Type:", self.type)
        print("Mileage:", self.mileage)


# Creating objects
print("Enter Car Details:")
car_obj = Car()
car_obj.getdetails()
car_obj.getCardetails()

print("\nEnter Bike Details:")
bike_obj = Bike()
bike_obj.getdetails()
bike_obj.getBikedetails()

# Displaying details
print("\n===== OUTPUT =====")
car_obj.display_info()
car_obj.display_car()

bike_obj.display_info()
bike_obj.display_bike()