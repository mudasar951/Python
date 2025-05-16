class User:
    def __init__(self, first_name, last_name, age, location, occupation):
        """Initialize user profile attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.occupation = occupation
        self.login_attempts = 0

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

    def describe_user(self):
        """Print a summary of the user's information."""
        print(f"\nUser Profile:")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Location: {self.location}")
        print(f"Occupation: {self.occupation}")

    def greet_user(self):
        """Print a personalized greeting to the user."""
        print(f"Hello, {self.first_name} {self.last_name}! Welcome back!")


class Privileges:
    def __init__(self,privileges=None):
        if privileges is None:
            privileges = []
        self.privileges = privileges

    def show_privileges(self):
        print(f"Privilages: ")
        if self.privileges:
            for privilege in self.privileges:
                print(f"- {privilege}")
        else:
            print(f"{self.first_name} {self.last_name} has no privileges")

class Admin(User):
    def __init__(self, first_name, last_name, age, location, occupation, privileges=None):
        super().__init__(first_name, last_name, age, location, occupation)
        self.privileges = Privileges(privileges)