# 10-1. Learning Python: Open a blank file in your text editor and write a few 
# lines summarizing what you’ve learned about Python so far. Start each line 
# with the phrase In Python you can. . . . Save the file as learning_python.txt in 
# the same directory as your exercises from this chapter. Write a program that 
# reads the file and prints what you wrote three times. Print the contents once by 
# reading in the entire file, once by looping over the file object, and once by stor
# ing the lines in a list and then working with them outside the with block.

filename = 'learning_python.txt'

# with open(filename) as file_object:
#     content = file_object.read()
#     print(content)

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

# with open(filename) as file_object:
#     lines = file_object.readlines()

# content = ''
# for line in lines:
#     content += line.strip()

# print(content)
