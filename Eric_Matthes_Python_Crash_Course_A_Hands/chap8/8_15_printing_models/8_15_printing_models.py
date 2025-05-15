# 8-15. Printing Models: Put the functions for the example printing_models.py in a 
# separate file called printing_functions.py. Write an import statement at the top 
# of printing_models.py, and modify the file to use the imported functions.

# printing_models.py

# Importing the functions from printing_functions.py
from printing_functions import print_models, show_completed_models

# Example usage
unprinted_designs = ['phone case', 'robot', 'drone']
completed_models = []

# Print the models
print_models(unprinted_designs, completed_models)

# Show completed models
show_completed_models(completed_models)
