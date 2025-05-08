# 5-2. More Conditional Tests: You don’t have to limit the number of tests you 
#create to ten. If you want to try more comparisons, write more tests and add 
#them to conditional_tests.py. Have at least one True and one False result for 
#each of the following:

# •	Tests for equality and inequality with strings
car = 'bmw'
print(car == 'bmw')
print(car != 'bmw')

# •	Tests using the lower() method
car = 'BMW'
print(car.lower() == 'bmw')
print(car.lower() != 'bmw')

# •	Numerical tests involving equality and inequality, greater than and 
#less than, greater than or equal to, and less than or equal to
num = 10
print(num == 9)
print(num != 9)
print(num > 9)
print(num < 9)
print(num >= 9)
print(num <= 9)

# •	Tests using the and keyword and the or keyword
num = 12
print(num > 10 and num < 20)
print(num > 10 or num ==10)

# •	Test whether an item is in a list
num = [1,2,3,4,5]
print(6 in num)

# •	Test whether an item is not in a list
num = [1,2,3,4,5]
print(6 not in num)


