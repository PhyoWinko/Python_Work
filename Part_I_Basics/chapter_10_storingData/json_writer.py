import json 

number_list = [12, 21, 36, 10, 8]

filename = "number.json"
with open(filename, "w") as file:
    json.dump(number_list, file)