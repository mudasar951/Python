# 6-5. Rivers: Make a dictionary containing three major rivers and the country 
#each river runs through. One key-value pair might be 'nile': 'egypt'.
rivers = {'nile':'egypt', 'indus':"pakistan", 'ganges':'india'}

# •	Use a loop to print a sentence about each river, such as The Nile runs 
#through Egypt.
for key in rivers.keys():
    print(f"The {key} runs through {rivers[key]}")

# •	Use a loop to print the name of each river included in the dictionary.
for key in rivers.keys():
    print(key)

# •	Use a loop to print the name of each country included in the dictionary.
for value in rivers.values():
    print(value)