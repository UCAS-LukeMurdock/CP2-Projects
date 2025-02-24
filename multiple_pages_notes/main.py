# Luke Murdock, Using Multiple Pages Notes


# 1. How do you make multiple files in python?
    # To make multiple python files you have to make a new file that has .py at the end.
    # snake_case file names
    # Descriptive file names (short)

# 2. How do you get a function from another file?
from calc import addition as add, subtraction as sub
    # aliasing is where you import a funciton and give it a new keyword
print(add())
print(sub())


# 3. How do you get variables from another file?
    # You can get variables the same way as functions but you should get it from the functions instead.
from calc import num
    # Better to return from a function

# 4. How do you have a function with multiple returns?
def get_user_info():
    name = input("What is your name:\n")
    age = input("What is your age:\n")
    color = input("What is your favorite color:\n")
    return name, age, color

name, quest, color = get_user_info()
print(quest)

# 5. Why would you use multiple pages for a python project? 
    # It is easier to merge github branches.
    # Modularity - breaking the program into smaller more managable pieces.
    # Functionality - keeps your code clean
    # 