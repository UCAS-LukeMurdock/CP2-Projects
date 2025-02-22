#Luke Murdock, Word Counter
#import 

'''
Uses at least 3 pages (main, file handling, and time handling) 
    Note: main is the only file name I've given you
Reads and Writes to the file
Uses functional decomposition
Lets the user tell what file to use it on
'''

def int_input(prompt, range = 0): # Checks and solves errors in integer inputs (Has Range If Needed)
    while True:
        try: 
            response = int(input(prompt).strip())
        except ValueError:
            print("Invalid Input Type")
            continue
        if range == 0 or (response > 0 and response <= range):
            break
        else:
            print("Not In Range")
            continue
    return response

def display(): # Prints the file's contents
    print("\n:\n")
    # for in :
        #print(f"- {}\n- {}\n- {}\n- {}\n")

def func1(): # 
    print("")

def main(): # Introduces the program and then lets the user choose one of the options
    print("Welcome, where you can see, add, remove, or search through it.")
    while True:
        choice = int_input("\nDisplay(1) Read(2) Write(3) (4) (5) Exit(6)\n", 6)
        if choice == 1:
            display()
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
