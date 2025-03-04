# Luke Murdock, Battle Simulator
'''
OVERVIEW:
Create a program that allows users to create, manage, and battle RPG characters. The program should use inner and helper functions to organize the code efficiently. Characters should be saved to and loaded from a CSV file.
REQUIREMENTS:
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
    Create a main menu for user interaction
File Operations:
    Save character data to a CSV file
    Load character data from a CSV file
Additional Features (Optional): (Note: only awarded IF all 20 points are earned, they cannot make up for lost points)
    Implement character classes (warrior, mage, rogue) with unique attributes 
        Implementation of basic character classes (e.g. warrior, mage, rouge) with slight variations in starting attributes (1 point)
        Implement character classes with unique abilities or skills (2 points)
    Add a simple inventory system 
        Allow characters to hold items (1 point)
        Inventory with equippable items that affect character stats (2 points)
        Advanced inventory system with item crafting or combining (3 points)
    Create special abilities for characters
        Implement one or two special abelites for characters (1 point)
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
import csv

def intput(prompt, min = 0, max = 0): # Checks and prompts user to solve errors in integer inputs (Has Range If Needed)
    try:
        response = int(input(prompt).strip())
    except:
        print("Not An Integer")
        response = intput(prompt,min,max)
    if (min != 0 and max != 0) and (response < min or response > max):
        print(f"Not In Range: {min}-{max}")
        response = intput(prompt,min,max)
    return response
age = intput("What is your age?\n")

def menu(): # Introduces the program and then lets the user choose one of the options
    print("Welcome, where you can see, add, remove, or search through it.")
    while True:
        choice = intput("\nDisplay(1) Search(2) Add(3) Remove(4) Edit(5) Exit(6)\n", 6)
        if choice == 1:
            create()
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
            print("Something Broke")
            continue
menu()