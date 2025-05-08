# 6-7. People: Start with the program you wrote for Exercise 6-1 (page 99). 
#Make two new dictionaries representing different people, and store all three 
#dictionaries in a list called people. Loop through your list of people. As you 
#loop through the list, print everything you know about each person.

person_1 = {'first_name':'Hannan', 'last_name':'Rasool', 'age':19, 'city':'Abu dabi'}
person_2 = {'first_name':'Alice', 'last_name':'Ram', 'age':19, 'city':'London'}
person_3 = {'first_name':'Bob', 'last_name':'Bobi', 'age':19, 'city':'Kirachi'}

people = [person_1, person_2, person_3]

for person in people:
    for key in person.keys():
        print(f"{key} = {person[key]}")
    print()
