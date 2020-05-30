def describe_pet(pet_name, animal_type='dog',):
    """Display information about a pet"""
    print (f"\nI have a {animal_type.title()}.")
    print (f"My {animal_type}'s name is {pet_name.title()}")

# A dog named willie
describe_pet('willie')
describe_pet(pet_name='willie')

# a hamster named harry
describe_pet('harry', animal_type='hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')