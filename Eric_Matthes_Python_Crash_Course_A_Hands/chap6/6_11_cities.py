# 6-11. Cities: Make a dictionary called cities. Use the names of three cities as 
#keys in your dictionary. Create a dictionary of information about each city and 
#include the country that the city is in, its approximate population, and one fact 
#about that city. The keys for each city’s dictionary should be something like 
#country, population, and fact. Print the name of each city and all of the infor
#mation you have stored about it.

cities = {
    'Lahore':{'country':'pakistan','population':13004135,'fact':'Cultural Heart of Pakistan'},
    'Delhi' :{'country':'india','population':34665600,'fact':'capital of India'}
    }

for city in cities.keys():
    print(f"Name = {city}")
    for key, value in cities[city].items():
        print(f"{key} = {value}")