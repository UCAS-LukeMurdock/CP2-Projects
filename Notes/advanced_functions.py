# Luke Murdock, Advanced Functions Notes

# 1. What is a helper function?
    # A function written to be called to be in another function
def is_int(user_input):
    try:
        int(user_input)
    except:
        # 8. What is recursion?
            # When you call a function inside of itself
        # 9. How does recursion work?
            # 
        print("Please give me a number")
        user_input = is_int(input("How old are you?\n"))
    return int(user_input)
    
def age():
    old = is_int(input("How old are you?\n"))

    print(f"Cool. You are {old}")
age()

# 2. What is the purpose of a helper function?
    # The purpose of a helper function is to break down a task into steps to make the funciton less bloated and to make ir more readable.
# 3. What is an inner function?
    # An inner function is a function that exists inside of another function
def add(a):
    b = int(input("Give me a number\n"))

    def addition():
        print(a+b)

    addition()

add(3)


import logging

logging.basicConfig(level=logging.INFO)

def logger(func):
    
    def wrapper(*args, **kwargs):
        logging.info(f"Excecuting {func.__name__} with {args}, {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@logger
def adder(a,b):
    return a+b

print(adder(3,4))

# 4. What is the scope of a variable in a function WITH an inner function?
    # It has access to all of the outer function's variables but not the other way.
# 5. Why do we use inner functions?
    # We use inner functions to keep the inner function safe and there will be less variables and returns.
    # It can be used for debugging also.
# 6. What is a closure function?
    # A closure function allows a function to remember values across mulitple calls
def add(a):

    def addition(b):
        return a+b

    return addition

base = add(10)

print(base(5))
#EXAMPLE
def math(income):

    def perc(amount, type):
        percent = amount/income
        print(f"Your {type} is ${amount}, and that is {percent} of your income")

def user_inputs():
    return int(input(f"What is your monthly {type}\n$"))

income = user_inputs("income")
rent = user_inputs("rent")
util = user_inputs("utilities")
groc = user_inputs("gorceries")
tansport = user_inputs("transportation")

start = math()

# 7. Why do we write closure functions?
    # We use closure functions because it saves information across multiple calls