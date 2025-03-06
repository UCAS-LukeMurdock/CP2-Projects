# Luke Murdock, 
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

def menu(): # Introduces the program and then lets the user choose one of the options
    print("Welcome, where you can see, add, remove, or search through it.")
    while True:
        choice = intput("\nDisplay(1) Search(2) Add(3) Remove(4) Edit(5) Exit(6)\n", 1,6)
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
menu()