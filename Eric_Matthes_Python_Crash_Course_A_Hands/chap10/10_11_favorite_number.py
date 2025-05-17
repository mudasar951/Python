# 10-11. Favorite Number: Write a program that prompts for the user’s favorite 
# number. Use json.dump() to store this number in a file. Write a separate pro
# gram that reads in this value and prints the message, “I know your favorite 
# number! It’s _____.”

# import json
# number = input("Enter your favorite number: ")

# with open('favorite_number.txt', 'w') as f:
#     json.dump(number, f)


import json

with open('favorite_number.txt', 'r') as f:
    favorite_number = json.load(f)
    print(f"I know your favorite number! It's {favorite_number}.")