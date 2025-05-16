#  9-15. Lottery Analysis: You can use a loop to see how hard it might be to win 
# the kind of lottery you just modeled. Make a list or tuple called my_ticket. 
# Write a loop that keeps pulling numbers until your ticket wins. Print a message 
# reporting how many times the loop had to run to give you a winning ticket.

import random

# Lottery setup
lottery_pool = [str(n) for n in range(10)] + list("ABCDE")
my_ticket = ['1', 'A', '3', 'C']

def get_random_ticket(pool, length=4):
    return random.sample(pool, length)

attempts = 0
won = False

while not won:
    drawn_ticket = get_random_ticket(lottery_pool)
    attempts += 1
    if drawn_ticket == my_ticket:
        won = True

print(f"Your ticket {my_ticket} won after {attempts} attempts!")
