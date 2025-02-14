#Luke Murdock, To Do List

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

# 
with open("To Do List\list.csv", "r") as file:
    pass

def display(): # Prints all of 
    print("\nTo-Do List:\n")
    for task in tasks:
        print(f"- {}\n- {}\n- {}\n- {}\n")

def add(): # 
    print("")

def mark(): # 
    print("")

def unmark(): # 
    print("")

def delete(): # 
    print("")

def main(): # Introduces the program and then lets the user choose one of the options
    print("Welcome to this to-do list program that lets you add, mark complete, unmark, or delete a task from the list")
    while True:
        choice = num_input("\nDisplay(1) Search(2) Add(3) Remove(4) Edit(5) Exit(6)\n", 6)
        if choice == 1:
            display()
        elif choice == 2:
            add()
        elif choice == 3:
            mark()
        elif choice == 4:
            unmark()
        elif choice == 5:
            delete()
        elif choice == 6:
            print("Come Back Soon!")
            break
        else:
            print("Something Broke")
            continue

main()