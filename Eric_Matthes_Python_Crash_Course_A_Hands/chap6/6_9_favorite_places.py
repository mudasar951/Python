#6-9. Favorite Places: Make a dictionary called favorite_places. Think of three 
#names to use as keys in the dictionary, and store one to three favorite places 
#for each person. To make this exercise a bit more interesting, ask some friends 
#to name a few of their favorite places. Loop through the dictionary, and print 
#each person’s name and their favorite places.

favorite_places = {
    'Alice':['London','Italy','Germany'],
    'Bob':['place_1','place_2', 'place_3'],
    'Ali':['place_x','place_y','place_z'],
    }

for name in favorite_places.keys():
    print(f"{name}'s favorite places are:")
    for place in favorite_places[name]:
        print(place)