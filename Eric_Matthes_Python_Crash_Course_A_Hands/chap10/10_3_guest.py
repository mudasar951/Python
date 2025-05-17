#  10-3. Guest: Write a program that prompts the user for their name. When they 
# respond, write their name to a file called guest.txt.

filename = 'guest.txt'

with open(filename, 'w') as file_object:
    name = input("Enter your name: ")
    file_object.write(f"{name}\n")
