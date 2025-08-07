import json

with open("number.json", "r") as file:
    numbers = json.load(file)

print(numbers)