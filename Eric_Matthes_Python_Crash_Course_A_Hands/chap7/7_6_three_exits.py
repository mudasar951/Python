#7-6. Three Exits: Write different versions of either Exercise 7-4 or Exercise 7-5 
#that do each of the following at least once:
# •	Use a conditional test in the while statement to stop the loop.
# •	Use an active variable to control how long the loop runs.
# •	Use a break statement to exit the loop when the user enters a 'quit' value.

topping = ''
while topping != 'quit':
    topping = input("Enter topping for your pizza or quit to quit: ")
    if topping != 'quit':
        print(f"{topping} is added to your pizza")

active = True
while active:
    topping = input("Enter topping for your pizza or quit to quit: ")
    if topping == 'quit':
        active = False
    else:
        print(f"{topping} is added to your pizza")

while True:
    topping = input("Enter topping for your pizza or quit to quit: ")
    if topping == 'quit':
        break
    else:
        print(f"{topping} is added to your pizza")