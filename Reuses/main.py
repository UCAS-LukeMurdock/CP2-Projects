
#inputs

def int_input(text): # Only takes in integers
    while True:
        try: output = int(input(text))
        except ValueError:
            print("Invalid Input! (only integers accepted)")
            input("Press enter to try again")
            continue
        return output
def str_input(text): # Only takes in strings
    while True:
        try: output = str(input(text))
        except ValueError:
            print("String Input! (only strings accepted)")
            input("Press enter to try again")
            continue
        return output
def float_input(text): # Only takes in floats
    while True:
        try: output = float(input(text))
        except ValueError:
            print("Invalid Input! (only floats accepted)")
            input("Press enter to try again")
            continue
        return output
def cs(): # Clear Screen
    print("\033c",end="")

choice = int_input()