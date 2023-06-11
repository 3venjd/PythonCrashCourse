def print_models(unprinted_designs,completed_models):
    """
    simulate printing each design, until none are left
    move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_desing = unprinted_designs.pop()
        print(f"Printing model : {current_desing}")
        completed_models.append(current_desing)

def show_completed_models(completed_models):
    #Display all completed models
    for completed_model in completed_models:
        print(completed_model)