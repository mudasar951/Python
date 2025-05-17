# 10-5. Programming Poll: Write a while loop that asks people why they like 
# programming. Each time someone enters a reason, add their reason to a file 
# that stores all the responses.

filename = 'responses.txt'

print("Welcome to programming poll. Press q to quit")

with open(filename, 'w') as file_object:
    while True:
        reason = input("Why you like Programming: ")
        if reason.lower() == 'q':
            break
        file_object.write(f"{reason}\n")