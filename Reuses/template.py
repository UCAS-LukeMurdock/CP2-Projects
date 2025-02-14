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

def func1(): # 
    print("")

def func2(): # 
    print("")

def func3(): # 
    print("")

def main(): # Introduces the program and then lets the user choose one of the options
    print("Welcome, where you can see, add, remove, or search through it.")
    while True:
        choice = num_input("\nDisplay(1) Search(2) Add(3) Remove(4) Edit(5) Exit(6)\n", 6)

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
            print("Something Broke")
            continue

main()