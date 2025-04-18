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

from file_handler import read_file, write_file
from pet_handler import ask_new_pet

def menu(): # Introduces the program and then lets the user choose one of the options
    while True:
        choice = input("\n (2) (3) (4) (5) Exit(6)\nChoice:").strip()
        if choice == '1':
            ()
        elif choice == '2':
            ()
        elif choice == '3':
            ()
        elif choice == '4':
            ()
        elif choice == '5':
            ()
        elif choice == '6':
            ()
        elif choice == '7':
            break
        else:
            print("\nInvalid Input (Insert a Corresponding Number)")

def pick_pet(): # 
    pets = read_file()
    for pet in pets:
        pet.active = False
    while True:
        choice = input("\nGet a pet(1) Interact with a pet(2) Quit(3)\nChoice: ").strip()
        if choice == '1':
            print(ask_new_pet())
        elif choice == '2':

            def pick_interact_pet():
                nonlocal pets
                found = False
                name = input('\nName of the pet: ').strip()
                for ind, user in enumerate(pets):
                    if name == user['Name']:
                        pets[ind].active = True
                        write_file(pets)
                        print('\nYou have picked a pet!')
                        found = True
                        menu()
                        pets = read_file()
                if found == False:
                    print(f'\nThe pet {name} could not be found')
                    continue

            pick_interact_pet()

        elif choice == '3':
            print("\n\n\nThank you for using this Pet Simulator!\nCome Back Soon!\n\n\n")
            exit()
        else:
            print('\nInvalid Input (Insert a Corresponding Number)')
            
            
print("\n\n\nWelcome to this Pet Simulator, where you can get pets, , , or .")
pick_pet()