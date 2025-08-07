import json

try:
    with open("username.json", "r") as file:
        user_name = json.load(file)
        print(f"Welcome back, {user_name} !!")

except FileNotFoundError:
    user_name = input("What's your name: ")
    with open("username.json", "w") as file:
        json.dump(user_name, file)
    print(f"We registered you as {user_name}")