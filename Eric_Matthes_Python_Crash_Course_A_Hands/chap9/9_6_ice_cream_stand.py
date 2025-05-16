#  9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant. Write 
# a class called IceCreamStand that inherits from the Restaurant class you wrote 
# in Exercise 9-1 (page 162) or Exercise 9-4 (page 167). Either version of 
# the class will work; just pick the one you like better. Add an attribute called 
# flavors that stores a list of ice cream flavors. Write a method that displays 
# these flavors. Create an instance of IceCreamStand, and call this method.

class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def set_number_served(self, no_served):
        self.number_served = no_served

    def increment_number_served(self, no_of_customer):
        self.number_served += no_of_customer

    def describe_restaurant(self):
        print(f"restaurant_name = {self.restaurant_name}, cuisine_type = {self.cuisine_type}")


    def open_restaurant(self):
        print(f"{self.restaurant_name} is open")


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, ice_cream_flavour=None):
        super().__init__(restaurant_name, cuisine_type)
        self.ice_cream_flavour = ice_cream_flavour

    def display_flavour(self):
        print("Ice Cream flavours: ")
        for flavour in self.ice_cream_flavour:
            print(flavour)


ice_cream_stand = IceCreamStand('restaurant_1','cuisine_type_1',['flavour_1','flavour_2'])

ice_cream_stand.display_flavour()