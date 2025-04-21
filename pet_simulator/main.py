# Luke Murdock, Pet Simulator

from pet_class import random
from file_handler import read_file, write_file, active_pet
from pet_handler import ask_new_pet, display_pets, breed

def menu(): # Lets the user choose one of the options and then might randomly pick a random event to enact
    pets = read_file()
    pet = active_pet(pets)

    while True:
        choice = input(f"\nWhat do you want to do with your pet named {pets[pet].name}?\nView status(1) Pet(2) Feed(3) Play(4) Compete(5) Shop(6) Sleep(7) Breed(8)  Exit(0)\nChoice: ").strip()
        if choice == '0':
            pets[pet].active = False
            write_file(pets)
            break
        elif choice == '1':
            pets[pet].status()
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
        choice = input("\nGet a pet(1) Interact with a pet(2)  Quit(3)\nChoice: ").strip()
        if choice == '1':
            print(ask_new_pet())
        elif choice == '2':

            def pick_interact_pet(): # Picks the pet the user wanted if it exists and then goes to the menu
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
            
            
input("\n\n\nWelcome to this Pet Simulator,\n\nIt lets you get pets and then interact with them by doing things such as:\n - Petting them\n - Feeding them\n - Playing with them\n - Letting them compete\n - Shopping for them\n - Letting them sleep\n\nIf you let your pet sleep, they will have time to process things and they might even grow older!\n(Your pet will level up if they feel well enough when growing up)\n\n[Press 'Enter' to Continue]\n")
pick_pet()
