#Luke Murdock, 

import csv

def num_input(prompt, range = 0, data_type = "int"): # Checks and solves errors in int and float inputs (Has Range If Needed)
    while True:
        try: 
            if data_type == "int":
                response = int(input(prompt).strip())
            elif data_type == "float":
                response = float(input(prompt).strip())
        except ValueError:
            print("Invalid Input Type")
            continue
        if range == 0 or (response > 0 and response <= range):
            break
        else:
            print("Not In Range")
            continue
    return response

def func1():
    print("")

def main(): # This funcion welcomes the user, then lets the user choose what they want to do
    print("Welcome to my library, where you can see, add, remove, or search through it.")
    while True:
        choice = num_input("\nSimple Display(1) Display All(2) Search(3) Add(4) Remove(5) Edit(6) Exit(7)\n", 7)

        if choice == 1:
            ()
        elif choice == 2:
            print("\nLibrary:")
            ()
        elif choice == 3:
            ()
        elif choice == 4:
            ()
        elif choice == 5:
            ()
        elif choice == 6:
            ()
        elif choice == 7:
            print("Come Back Soon!")
            break
        else:
            print("Something Broke")
            continue