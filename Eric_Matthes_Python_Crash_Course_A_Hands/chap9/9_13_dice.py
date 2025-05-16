#  9-13. Dice: Make a class Die with one attribute called sides, which has a default 
# value of 6. Write a method called roll_die() that prints a random number 
# between 1 and the number of sides the die has. Make a 6-sided die and roll it 
# 10 times.
#  Make a 10-sided die and a 20-sided die. Roll each die 10 times.

from random import randint

class Die:
    def __init__(self, sides=6):
        self.sides = sides
        
    def roll_die(self):
        print(randint(1,self.sides))


die_1 = Die(6)

print("6-sided die rolling 10 times")
for i in range(1,11):
    die_1.roll_die()

die_2 = Die(10)

print("10-sided die rolling 10 times")
for i in range(1,11):
    die_2.roll_die()

die_3 = Die(20)

print("20-sided die rolling 10 times")
for i in range(1,11):
    die_3.roll_die()