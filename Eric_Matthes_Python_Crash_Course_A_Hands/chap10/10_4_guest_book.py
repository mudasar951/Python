# 10-4. Guest Book: Write a while loop that prompts users for their name. When 
# they enter their name, print a greeting to the screen and add a line recording 
# their visit in a file called guest_book.txt. Make sure each entry appears on a 
# new line in the file.

filename = 'guest_book.txt'

with open(filename, 'w') as file_object:
    while True:
        name = input("Enter your name: ")
        print(f"Hi {name}")
        file_object.write(f"{name}\n")
        choice = input("You want to quit yes/no: ")
        if choice == 'yes':
            break