# Luke Murdock, Updated Battle Simulator

from file_handler import intput
from character_handler import create, display, remove
from battle_file import battle
from store import shop, equip

def menu(): # Introduces the program and then lets the user choose one of the options
    print("\n\nWelcome to this Battle Simulator, where you can create, see, remove, shop for, or fight RPG characters.")
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