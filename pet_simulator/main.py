# Luke Murdock, Pet Simulator

"""
Create a Pet Simulator using Python classes. This project will focus on object-oriented programming concepts, implementing game-like logic, and creating a simple text-based user interface. Students will design a system to manage virtual pets, their attributes, and interactions.
REQUIRED ELEMENTS:

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

    
BONUS:
    
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

class pet:
    def __init__(self,name,species,age,hunger):
        self.name = name
        self.species = species
        self.age = age
        self.hunger = hunger
        self. = 
        self. = 
        self. = 
    def __str__(self):
        (f'\nName: {self.name}\nPeriod: {self.species}\nTeacher: {self.age}\nRoom: {self.hunger}')



def menu(): # Introduces the program and then lets the user choose one of the options
    print("\n\nWelcome, where you can see, add, remove, or search through it.")
    while True:
        choice = input("\nDisplay(1) Search(2) Add(3) Remove(4) Edit(5) Exit(6)\n", 1,6)
        if choice == 1:
            ()
        elif choice == 2:
            ()
        elif choice == 3:
            ()
        elif choice == 4:
            ()
        elif choice == 5:
            ()
        elif choice == 6:
            print("Come Back Soon!")
            break
        else:
            print("Invalid Input (Insert an Accepted Number)")
menu()

"""
Figure out how to manage the classes
Add class converter
Create project

"""