#7-10. Dream Vacation: Write a program that polls users about their dream vaca
#tion. Write a prompt similar to If you could visit one place in the world, where 
#would you go? Include a block of code that prints the results of the poll.

places = {}
poll_active = True
while poll_active:
    name = input("Enter your name: ")
    place = input("If you could visit one place in the world, where would you go? ")
    places[name] = place
    repeat = input("Enter quit to quit poll: ")
    if repeat == 'quit':
        poll_active =False

for name, place in places.items():
    print(f"{name} wand to visit {place}")