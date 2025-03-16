# Luke Murdock, Battle Simulator
'''
OVERVIEW:
    Create a program that allows users to create, manage, and battle RPG characters.
Character Creation and Management:
    Create new characters with attributes (name, health, strength, defense, speed)
    Save characters to a CSV file
    Load characters from a CSV file
    Display character information
Battle System:
    Implement a turn-based battle system between two characters
    Calculate damage based on character attributes
    Include a simple leveling system where characters gain experience after battles
Program Structure:
    Use inner functions for main features (character creation, battle system, menu)
    Implement helper functions for repetitive tasks (save/load, display character info)

Additional Features (Optional): (Note: only awarded IF all 20 points are earned, they cannot make up for lost points)
    Implement character classes (warrior, mage, rogue) with unique attributes 
        Implementation of basic character classes (e.g. warrior, mage, rouge) with slight variations in starting attributes (1 point)
        Implement character classes with unique abilities or skills (2 points)
    Add a simple inventory system 
        Allow characters to hold items (1 point)
        Inventory with equippable items that affect character stats (2 points)
        Advanced inventory system with item crafting or combining (3 points)
    Create special abilities for characters
        Implement one or two special abilites for characters (1 point)
        Implement a diverse set of special abilities that significantly impact battles (2 points)
    Enhanced Battle System
        Add status effects (e.g. poison, stun, frozen) to the battle system
        Implement a more complex battle system with multiple characters per side (3 points)
NOTES:
Focus on using inner and helper functions to organize your code
Ensure your program handles potential errors (e.g., file not found, invalid user input)
Comments for explanation of functions and any complex logic
Test your program thoroughly to ensure all features work as expected
'''
from file_handler import intput
from character_handler import create, display, remove
from battle_file import battle
from store import shop, equip

def menu(): # Introduces the program and then lets the user choose one of the options
    print("\n\nWelcome to this Battle Simulator, where you can create, see, remove, or fight RPG characters.")
    while True:
        choice = intput("\nCreate(1) Display(2) Remove(3) Fight(4) Shop(5) Equip Sword(6) Exit(7)\n", 1,7)
        if choice == 1:
            create()
        elif choice == 2:
            display()
        elif choice == 3:
            remove()
        elif choice == 4:
            battle()
        elif choice == 5:
            shop()
        elif choice == 6:
            equip()
        elif choice == 7:
            print("Come Back Soon!")
            break
        else:
            print("Something Broke")
            continue
menu()