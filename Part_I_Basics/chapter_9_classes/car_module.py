class Car():

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0 # attribute setting default value sometimes you can set even empty string

    def descriptive_name(self):
        return f"{self.year} {self.make} {self.model}"
    
    def read_odometer(self):
        print(f"This car has {self.odometer} miles on it.")

    def update_odometer(self, mile):
        if mile > self.odometer: # make sure you can't roll back mile or rewrite
            self.odometer = mile
        else:
            print("You can't roll back!")

    def increment_odometer(self, mile):
        self.odometer += mile
    
""" Here comes Inheritances now """

class Battery():
    def __init__(self, battery=75):
        self.battery = battery

    def describe_battery(self):
        print(f"This car has {self.battery} KWh battery.")

    def get_range(self):
        if self.battery == 75:
            range = 230
        elif self.battery == 80:
            range = 240
        print(f"this car can go approxiamtely {range} miles on a full charge.")

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year) #super mean parent super class, child subclass
        # super function make python connect parent and child class
        self.battery = Battery()

