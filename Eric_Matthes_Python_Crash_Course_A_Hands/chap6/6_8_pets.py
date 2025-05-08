#6-8. Pets: Make several dictionaries, where each dictionary represents a differ
#ent pet. In each dictionary, include the kind of animal and the owner’s name. 
#Store these dictionaries in a list called pets. Next, loop through your list and as 
#you do, print everything you know about each pet.

pet_1 = {'animal_kind':'dog', 'owner_name':'Alice'}
pet_2 = {'animal_kind':'cat', 'owner_name':'Bob'}
pet_3 = {'animal_kind':'Horse', 'owner_name':'Mudasar'}

pets = [pet_1, pet_2, pet_3]

for pet in pets:
    for key, vlaue in pet.items():
        print(f"{key} = {vlaue}")