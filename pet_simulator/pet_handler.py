# Luke Murdock, Pet Handler
from file_handler import read_file, write_file, active_pet
from pet_class import Pet, random

def display_pets(pets): # Displays all pet names and lets the user choose one
    print("\nPets:")
    for pet in pets:
        print(pet.name)
    return input("\nChoice: ").strip()

def create_pet(name, species, color, eye_color, age): # Takes parameters and starting stats to create a new pet
    pets = read_file()
    new_pet = Pet(name,species,color,eye_color,age, 0,0,0,["Collar"], 50,50,50, False)
    pets.append(new_pet)
    write_file(pets)

def ask_new_pet(): # Asks the user for details of their new pet that they will get and then creates it
    species = input("What species do you want this pet to be?: ").strip()
    color = input("What color do you want this pet to be?: ").strip()
    name = input("What do you want to name this pet?: ").strip().title()
    if species == '' or color == '' or name == '':
        return "\nInvalid Input (One of your inputs were empty)"
    age = random.randint(0,20)
    eye_color = random.choice(["red","orange","yellow","green","blue","purple",])
    create_pet(name, species, color, eye_color, age)
    return f"\nYou run into the wilderness and find a {color} {species.lower()} with {eye_color} eyes that looks {age} year{'s' if age != 1 else ''} old. You put a collar on it that says {name}."

def breed(): # If two pets are old enough then they can breed with each other to make a new pet that has both of their traits
    pets = read_file()
    pet = active_pet(pets)
    if pets[pet].age < 10:
        return f"{pets[pet].name} is too young to breed. (Breeding age limit is 10 years old)"
    print(f"\nWhat other pet do you want to breed with {pets[pet].name}?: ")
    name = display_pets(pets)
    if name.lower() == pets[pet].name.lower():
        return "\nYou can't breed a pet with itself"
    for ind, search_pet in enumerate(pets):
        if name.lower() == search_pet.name.lower():
            if search_pet.age < 10:
                return f"{search_pet.name} is too young to breed. (Breeding age limit is 10 years old)"
            other_pet = ind
            break

    species = random.choice([pets[pet].species, pets[other_pet].species])
    color = random.choice([pets[pet].color, pets[other_pet].color])
    eye_color = random.choice([pets[pet].eye_color, pets[other_pet].eye_color])
    create_pet("Newborn", species, color, eye_color, 0)
    return f"\n{pets[pet].name} bred with {pets[other_pet].name} to have a baby pet {species} that is {color} and has {eye_color} eyes. You give the new pet a collar that has no name yet.\n(Rename this pet by interacting with it and then going to view status)"
