import json

username_file = "username_file.json"

def get_new_username():
    username = input("What's your name: ")
    with open(username_file, "w") as file:
        json.dump(username, file)
        return username

def get_stored_username():
    try: 
        with open(username_file, "r") as file:
            username = json.load(file)
            return username
    except FileNotFoundError:
        return None

def greet_user():
    username = get_stored_username()
    if username:
        print(f"Welcome back, {username} !!!")
    if not username:
        username = get_new_username()
        print(f"Welcome, {username} !!!")

greet_user()