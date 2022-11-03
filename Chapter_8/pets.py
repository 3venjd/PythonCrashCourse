#def describe_pet(animal_type, pet_name):
#    """Display information about pet"""
#    print(f"\nI have a {animal_type}")
#    print(f"My {animal_type}'s name is {pet_name.title()}")

def describe_pet(pet_name, animal_type = "fish"):
    """Display information about pet"""
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}")


#describe_pet('hamster','harry')
describe_pet(animal_type = 'dog',pet_name = 'oddy')
describe_pet(pet_name="willie")