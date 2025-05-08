#6-10. Favorite Numbers: Modify your program from Exercise 6-2 (page 99) 
#so each person can have more than one favorite number. Then print each per
#son’s name along with their favorite numbers.

favorite_numbers = {
    'Alice': [1,4,7],
    'Bob': [3,6,2],
    'Charlie': [6],
    'David': [7,9,0],
    'Emma': [1,3,2]
}

for person in favorite_numbers:
    print(f"{person}'s favorite numbers are:")
    for num in favorite_numbers[person]:
        print(num)
