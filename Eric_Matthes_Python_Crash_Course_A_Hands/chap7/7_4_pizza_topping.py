# 7-4. Pizza Toppings: Write a loop that prompts the user to enter a series of 
#pizza toppings until they enter a 'quit' value. As they enter each topping, 
#print a message saying you’ll add that topping to their pizza.

while True:
    topping = input("Enter topping for your pizza or quit to quit: ")
    if topping == 'quit':
        break
    else:
        print(f"{topping} is added to your pizza")