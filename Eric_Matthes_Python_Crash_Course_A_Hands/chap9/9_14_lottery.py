# 9-14. Lottery: Make a list or tuple containing a series of 10 numbers and 
# five letters. Randomly select four numbers or letters from the list and print a 
# message saying that any ticket matching these four numbers or letters wins a 
# prize.

from random import choice

tickets = [1,2,3,4,5,6,7,8,9,10,'a','b','c','d','e']

print("Any ticket matching these four numbers or letters wins a prize.")

for _ in range(4):
    print(choice(tickets), end=' ')