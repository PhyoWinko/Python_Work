from random import randint
import pyttsx3

engine = pyttsx3.init()

class Dice():
    def __init__ (self, sides=6):
        self.sides = int(sides)

    def roll_dice(self):
        x = randint(1, self.sides)
        return x

sided_dice = int(input("Choose which sided dice you want to roll: "))
casio_dice = Dice(sided_dice)

n = int(input("how many times you want roll a dice: "))
for i in range(n):

    result = casio_dice.roll_dice()
    print(f"{i+1} time result : {result}")
    engine.say(f"{i+1} time result {result}")
    engine.runAndWait()