#  Reuses

def any_input(prompt, data_type): # Checks and solves errors in int and float inputs
    while True:
        try: 
            if data_type == "int":
                response = int(input(prompt))
            elif data_type == "float":
                response = float(input(prompt))
        except ValueError:
            print("Invalid Input Type")
            continue
        return response


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