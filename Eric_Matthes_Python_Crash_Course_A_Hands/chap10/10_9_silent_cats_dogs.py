# 10-9. Silent Cats and Dogs: Modify your except block in Exercise 10-8 to fail 
# silently if either file is missing.

try:
    with open('cats.txt') as f:
        content = f.read()
        print(content)
    
    with open('dogs.txt') as f:
        content = f.read()
        print(content)
    
except FileNotFoundError:
    pass