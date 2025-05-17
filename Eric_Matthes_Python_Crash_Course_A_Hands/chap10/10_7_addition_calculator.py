# 10-7. Addition Calculator: Wrap your code from Exercise 10-6 in a while loop 
# so the user can continue entering numbers even if they make a mistake and 
# enter text instead of a number.

print("Enter 'q' to quit")
while True:
    try:
        num_1 = input("Enter first number: ")
        if num_1 == 'q':
            break
        num_2 = input("Enter second number: ")
        if num_2 == 'q':
            break
        print(int(num_1)+int(num_2))
    except ValueError:
        print("Please enter only number!")