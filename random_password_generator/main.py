#Luke Murdock, Random Password Generator

import random, string

def any_input(prompt, data_type):
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

def main(): # IDK
    upper = any_input("Do you want the password to include uppercase letters?:\n", "int")

def upper(): # 

def lower(): # 


def num(): # 

def spec(): # 
