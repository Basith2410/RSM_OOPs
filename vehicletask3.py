# 3. Vehicle Class Hierarchy:
# You are developing a vehicle management system. You create a base class called Vehicle with attributes make, model, and year. 
# You implement methods to start the vehicle, stop the vehicle, and display its information. 
# You derive subclasses for different types of vehicles: Car, Motorcycle, and Truck. 
# In the Car class, you add attributes like num_doors and fuel_type. 
# In the Motorcycle class, you add an attribute top_speed. In the Truck class, you add attributes like cargo_capacity and num_axles. 
# You create instances for a car named myCar, a motorcycle named myMotorcycle, and a truck named myTruck. 
# You perform operations like starting, stopping, and displaying information for these vehicles.

class Vehicle():
    def __init__(x,make,model,year):
        x.make = make
        x.model = model
        x.year = year
    
    def start(x):
        print("Start")
    
    def stop(x):
        print("Stop")

    def display_info(x):
        print("Vehicle Information:")
        print("Make:", x.make)
        print("Model:", x.model)
        print("Year:", x.year)

class Car(Vehicle):
    def __init__(x, make, model, year, num_doors, fuel_type):
        super().__init__(make, model, year)
        x.num_doors = num_doors
        x.fuel_type = fuel_type

class Motorcycle(Vehicle):
    def __init__(x, make, model, year, top_speed):
        super().__init__(make, model, year)
        x.top_speed = top_speed

class Truck(Vehicle):
    def __init__(x, make, model, year, cargo_capacity, num_axles):
        super().__init__(make, model, year)
        x.cargo_capacity = cargo_capacity
        x.num_axles = num_axles

myCar = Car("Audi", "A6", 2022, 4, "Petrol")
myMotorcycle = Motorcycle("Honda", "Activa", 2023, 120)
myTruck = Truck("Tata", "Tacoma", 2021, "1000 Kg", 2)

myCar.start()
myCar.display_info()
myCar.stop()

print()

myMotorcycle.start()
myMotorcycle.display_info()
myMotorcycle.stop()

print()

myTruck.start()
myTruck.display_info()
myTruck.stop()




