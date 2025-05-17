# 10-6. Addition: One common problem when prompting for numerical input 
# occurs when people provide text instead of numbers. When you try to convert 
# the input to an int, you’ll get a ValueError. Write a program that prompts for 
# two numbers. Add them together and print the result. Catch the ValueError if 
# either input value is not a number, and print a friendly error message. Test your 
# program by entering two numbers and then by entering some text instead of a 
# number.

try:
    num_1 = input("Enter first number: ")
    num_2 = input("Enter second number: ")
    print(int(num_1)+int(num_2))
except ValueError:
    print("Please enter only number!")