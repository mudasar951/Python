#4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1 
#(page 56). Make a copy of the list of pizzas, and call it friend_pizzas. 
#Then, do the following:
# •	Add a new pizza to the original list.
# •	Add a different pizza to the list friend_pizzas.
# •	Prove that you have two separate lists. Print the message My favorite 
#pizzas are:, and then use a for loop to print the first list. Print the message 
#My friend’s favorite pizzas are:, and then use a for loop to print the sec
#ond list. Make sure each new pizza is stored in the appropriate list.

my_foods = ['pizza', 'falafel', 'carrot cake']
your_foods = my_foods[:]

my_foods.append("ice_cream")
your_foods.append("apple_juice")

print("My favorite foods:")
for food in my_foods:
    print(food)

print("My friends favorite food:")
for food in your_foods:
    print(food)

