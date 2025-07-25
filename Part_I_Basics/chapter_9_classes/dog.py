class Dog(): # Covention : capitalized refer to Class
    """ A simple attempt to model a dog. """

    def __init__(self, Name, Age): #init method
        self.name = Name
        self.age = Age

    def sit(self):
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        print(f"{self.name} is now rolling over !!!!!!!!!!!!!")

# Python automatically call init method and returns instance
my_dog = Dog("Aung Net", 2) # an instance of Dog
my_dog.sit()
my_dog.roll_over()

print("now you see how class work")

print(f"My dog name is {my_dog.name.title()}")
print(f"My dog age is {my_dog.age} years old.")

#  You’ll see this structure throughout this chapter and have lots of time to get used to it

# When attributes and methods have been
# given appropriately descriptive names like name, age, sit(), and roll_over(),
# we can easily infer what a block of code, even one we’ve never seen before,
# is supposed to do.

Bo_Phyu = Dog("Bo Phyu", 5)
print(f"His dog name is {Bo_Phyu.name.title()}")
Bo_Phyu.sit()
Bo_Phyu.roll_over()

# You can make as many instances from one class as you need