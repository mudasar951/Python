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