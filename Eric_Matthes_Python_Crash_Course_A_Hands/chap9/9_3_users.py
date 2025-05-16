# 9-3. Users: Make a class called User. Create two attributes called first_name 
# and last_name, and then create several other attributes that are typically stored 
# in a user profile. Make a method called describe_user() that prints a summary 
# of the user’s information. Make another method called greet_user() that prints 
# a personalized greeting to the user.
#  Create several instances representing different users, and call both methods 
# for each user.

# user.py

class User:
    def __init__(self, first_name, last_name, age, location, occupation):
        """Initialize user profile attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.occupation = occupation

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

# Creating instances of User
user1 = User("Alice", "Johnson", 28, "New York", "Graphic Designer")
user2 = User("Ben", "Martinez", 35, "Los Angeles", "Software Developer")
user3 = User("Claire", "Nguyen", 22, "Seattle", "Student")

# Calling methods for each user
user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()

        