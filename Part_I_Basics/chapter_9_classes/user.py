class User():

    def __init__ (self, first_name, second_name, Country):
        self.first_name = first_name
        self.second_name = second_name
        self.country = Country

        self.login_attempt = 1

    def describe_user(self):
        print(f"{self.first_name} {self.second_name}")

    def greet_user(self):
        print(f"Bonjour, our valuable user, {self.first_name} from {self.country}")

    def increment_login_attempts(self):
        self.login_attempt += 1

    def reset_login_attempt(self):
        self.login_attempt = 0

    def show_login_attempt(self):
        print(f"login attempt {self.login_attempt}")

user_1 = User("Franklin", "Reechard", "USA")
user_1.describe_user()
user_1.greet_user()

""" OK now log in attempt """

user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.show_login_attempt()

user_1.reset_login_attempt()
user_1.show_login_attempt()