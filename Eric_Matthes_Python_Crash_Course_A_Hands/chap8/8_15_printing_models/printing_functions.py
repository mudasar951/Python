# printing_functions.py

def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design until there are no unprinted designs.
    After each design is printed, move it to completed_models.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Show all the models that have been printed."""
    print("\nThe following models have been printed:")
    for model in completed_models:
        print(f"- {model}")
