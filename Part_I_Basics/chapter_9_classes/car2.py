# instance as attribute

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
    
my_car = Car("Toyata", "Rush", 2020) # my car instance
print(my_car.descriptive_name())
my_car.read_odometer()

my_car.update_odometer(25000)
my_car.read_odometer()

my_car.update_odometer(100)
my_car.read_odometer()

my_car.increment_odometer(1000)
my_car.read_odometer()

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

my_new_tesla = ElectricCar("Tesla", "model s", 2016) # my_new_tesla instance
print(my_new_tesla.descriptive_name())
my_new_tesla.battery.describe_battery()
my_new_tesla.battery.get_range() # when we want to call the method, we have to call it through car battery attribute