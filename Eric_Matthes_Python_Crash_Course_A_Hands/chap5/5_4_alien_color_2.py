#5-4. Alien Colors #2: Choose a color for an alien as you did in Exercise 5-3, and 
#write an if-else chain.
alien_color = 'green'

# •	If the alien’s color is green, print a statement that the player just earned 
#5 points for shooting the alien.
if alien_color=='green':
    print("Player earned 5 points")

# •	If the alien’s color isn’t green, print a statement that the player just earned 
#10 points.
elif alien_color != 'green':
    print("player just earned 10 points")

# •	Write one version of this program that runs the if block and another that 
#runs the else block.
if alien_color == 'green':
    print("Player earned 5 points")
else:
    print("player just earned 10 points")


