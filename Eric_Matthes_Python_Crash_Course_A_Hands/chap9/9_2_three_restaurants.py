# 9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three 
# different instances from the class, and call describe_restaurant() for each 
# instance.

class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"restaurant_name = {self.restaurant_name}, cuisine_type = {self.cuisine_type}")


    def open_restaurant(self):
        print(f"{self.restaurant_name} is open")


restaurant_1 = Restaurant('restaurant_1','cuisine_type_1')
restaurant_2 = Restaurant('restaurant_2','cuisine_type_2')
restaurant_3 = Restaurant('restaurant_3','cuisine_type_3')


restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()
