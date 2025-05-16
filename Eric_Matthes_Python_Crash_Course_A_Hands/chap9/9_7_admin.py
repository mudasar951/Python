# 9-7. Admin: An administrator is a special kind of user. Write a class called 
# Admin that inherits from the User class you wrote in Exercise 9-3 (page 162) 
# or Exercise 9-5 (page 167). Add an attribute, privileges, that stores a list 
# of strings like "can add post", "can delete post", "can ban user", and so on. 
# Write a method called show_privileges() that lists the administrator’s set of 
# privileges. Create an instance of Admin, and call your method.

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


class Admin(User):
    def __init__(self, first_name, last_name, age, location, occupation, privileges=None):
        super().__init__(first_name, last_name, age, location, occupation)
        if privileges is None:
            privileges = []
        self.privileges = privileges

    def show_privileges(self):
        print(f"{self.first_name} {self.last_name} has following privilages: ")
        if self.privileges:
            for privilege in self.privileges:
                print(f"- {privilege}")
        else:
            print(f"{self.first_name} {self.last_name} has no privileges")


user = Admin("Alice", "Johnson", 28, "New York", "Graphic Designer",['can add post', 'can delete post', 'can ban user'])

user.show_privileges()