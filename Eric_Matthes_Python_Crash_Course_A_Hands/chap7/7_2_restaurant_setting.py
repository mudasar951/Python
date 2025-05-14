#7-2. Restaurant Seating: Write a program that asks the user how many people 
#are in their dinner group. If the answer is more than eight, print a message say
#ing they’ll have to wait for a table. Otherwise, report that their table is ready.

num_of_people = input("how many people are in your dinner group: ")
num_of_people = int(num_of_people)

if num_of_people > 8:
    print("You have to wait for a table.")
else:
    print("Your table is ready.")