# Luke Murdock, Pet Handler
import random
from file_handler import Pet, read_file, write_file

def ask_new_pet(): # 
    species = input("What species do you want this pet to be?: ").strip().title()
    color = input("What color do you want this pet to be?: ").strip()
    name = input("What do you want to name this pet?: ").strip().title()
    age = random.randint(0,20)
    eye_color = random.choice(["red","orange","yellow","green","blue","purple",])
    create_pet(name, species, color, eye_color, age)
    print(f"\nYou run into the wilderness and find a {color} {species.lower()} with {eye_color} eyes that looks {age} year{'s' if age != 1 else ''} old. You put a collar on it that says {name}.")

def create_pet(name, species, color, eye_color, age): # 
    pets = read_file()
    new_pet = Pet(name,species,color,eye_color,age, 0,0,["Collar"], 100,100,100,100) # Fix stats
    pets.append(new_pet)
    write_file(pets)