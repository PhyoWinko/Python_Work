from car_module import Car, ElectricCar, Battery

my_beetle_car = Car("Volkswagen", "Beetle", 2017)
print(my_beetle_car.descriptive_name())

my_electric_car = ElectricCar("Tesla", "Model s", 2000)
print(my_electric_car.descriptive_name())
my_electric_car.battery.describe_battery()