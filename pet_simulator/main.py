# Luke Murdock, Pet Simulator

"""
Create a Pet Simulator using Python classes. This project will focus on object-oriented programming concepts, implementing game-like logic, and creating a simple text-based user interface. Students will design a system to manage virtual pets, their attributes, and interactions.
|| REQUIRED ELEMENTS:
Class Implementation:
    Create a Pet class with attributes such as name, species, age, hunger, happiness, and energy
    Implement methods for feeding, playing, and putting the pet to sleep
    Include a method to check and display the pet's status
Pet Interactions:
    Develop a system where each action (feeding, playing, sleeping) affects multiple attributes
    Implement a time system where each action advances time
    Create different food types that affect hunger and happiness differently
User Interface:
    Design a text-based menu for interacting with pets
    Allow users to create multiple pets and switch between them
    Include options to perform various actions with the selected pet
Game Logic:
    Implement a health attribute that changes based on how well the pet is cared for
    Create events that occur randomly (e.g., pet gets sick, finds a toy)
    Add a leveling system where pets can learn new skills as they grow
Data Management:
    Implement a simple save/load system to store pet data between sessions

Bonus are only available to projects submitted on time that meet ALL of the minimum requirements.
|| BONUS:
| Pet Breeding System 
    Create a system where two pets can breed to create a new pet with combined characteristics. (3 points)
    | Implement genetic traits that can be passed down to offspring. (4 points)
    Implement a family tree visualization for pets (5 points)

| Pet Shop and Economy Add a virtual currency system
    Implement a virtual currency and economy system (3 points)
    Create a pet shop with various items for purchase (4 points)
    Design an inventory system for managing purchased items (5 points)

| Pet Competition Events (e.g., races, talent shows)
    Create a pet competition system with multiple event types (3 points)
    Implement a scoring and reward system for competitions (4 points)
    Design a leaderboard and pet ranking system (5 points)
"""
from pet_class import random
from file_handler import read_file, write_file, active_pet
from pet_handler import ask_new_pet, display_pets, breed

def menu(): # Lets the user choose one of the options and then might randomly pick a random event to enact
    pets = read_file()
    pet = active_pet(pets)

    while True:
        choice = input(f"\nWhat do you want to do with your pet named {pets[pet].name}?\nView status(1) Pet(2) Feed(3) Play(4) Compete(5) Shop(6) Sleep(7) Breed(8) Exit(0)\nChoice: ").strip()
        if choice == '0':
            pets[pet].active = False
            write_file(pets)
            break
        elif choice == '1':
            print(pets[pet].status())
        elif choice == '2':
            print(pets[pet].pet())
        elif choice == '3':
            print(pets[pet].feed())
        elif choice == '4':
            print(pets[pet].play())
        elif choice == '5':
            print(pets[pet].competition())
        elif choice == '6':
            print(pets[pet].shop())
        elif choice == '7':
            print(pets[pet].sleep())
        elif choice == '8':
            print(breed())
            pets = read_file()
        else:
            print("\nInvalid Input (Insert a Corresponding Number)")
        if random.randint(1,10) == 10:

            sick_weight = round((50 - pets[pet].health)/10)*2
            if sick_weight <= 0:
                sick_weight = 1

            event = random.choices(["Sick","Toy","Money","Stat"],weights = [sick_weight,2,2,2])
            if event == ["Sick"]:
                print(pets[pet].sick())
            elif event == ["Toy"]:
                print(pets[pet].find_toy())
            elif event == ["Money"]:
                print(pets[pet].find_money())
            elif event == ["Stat"]:
                print(pets[pet].stat_burst())
        write_file(pets)

def pick_pet(): # Lets a user get new pets and pick which one they want to interact with
    pets = read_file()
    for ind, pet in enumerate(pets):
        pets[ind].active = False
    write_file(pets)
    while True:
        choice = input("\nGet a pet(1) Interact with a pet(2) Quit(3)\nChoice: ").strip()
        if choice == '1':
            print(ask_new_pet())
        elif choice == '2':

            def pick_interact_pet():
                nonlocal pets
                name = display_pets(pets)
                for ind, pet in enumerate(pets):
                    if name.lower() == pet.name.lower():
                        pets[ind].active = True
                        write_file(pets)
                        print(f'\nYou have successfully picked your pet, {pets[ind].name}!')
                        return True
                print(f'\nThe pet "{name}" could not be found')
                return False
                    
            if pick_interact_pet() == True:
                menu()

        elif choice == '3':
            print("\n\n\nThank you for using this Pet Simulator!\nCome Back Soon!\n\n\n")
            exit()
        else:
            print('\nInvalid Input (Insert a Corresponding Number)')
        pets = read_file()
            
            
print("\n\n\nWelcome to this Pet Simulator, where you can get pets and then interact with them by doing things with them, such as petting them, feeding them, or playing with them.\nIf you let your pet sleep, they will have time to process things and they might even grow older!\n(Your pet will level up if they feel well enough when growing up)")
pick_pet()

# Testing, Spacing, README
# Get rid of random comments and stuff
# Add Stupid-Proofing with names, Color Mixing