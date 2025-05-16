# 9-5. Login Attempts: Add an attribute called login_attempts to your User 
# class from Exercise 9-3 (page 162). Write a method called increment_login 
# _attempts() that increments the value of login_attempts by 1. Write another 
# method called reset_login_attempts() that resets the value of login_attempts 
# to 0.
#  Make an instance of the User class and call increment_login_attempts() 
# several times. Print the value of login_attempts to make sure it was incremented 
# properly, and then call reset_login_attempts(). Print login_attempts again to 
# make sure it was reset to 0.


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


user1 = User("Alice", "Johnson", 28, "New York", "Graphic Designer")

user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()

print(user1.login_attempts)

user1.reset_login_attempts()

print(user1.login_attempts)

