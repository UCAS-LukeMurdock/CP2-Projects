# Luke Murdock, Coin Change Problem
"""
Create a program that allows users to solve the Coin Change Problem by inputting a target amount and the available coin denominations. The program should load the coin denominations from a file based on the user's input of a country and then calculate the minimum number of coins needed to make the target amount. The program should also display the names of the coins used in the solution.
Coin Denomination File:
    Create a text or CSV file that contains the coin denominations for different countries.
    Comma-separated list of coin names and values (e.g., "Penny-1,Nickel-5,Dime-10,Quarter-25").
Coin Change Problem:
    Implement the logic to solve the Coin Change Problem using the provided coin denominations.
    The program should handle various edge cases, such as negative or zero target amounts, and invalid coin denominations.
User Interaction:
    Prompt the user to enter the country for which they want to solve the Coin Change Problem.
    Prompt the user to enter the target amount.
    Display the minimum number of coins needed to make the target amount, as well as the names of the coins used.
Program Structure:
    Use inner functions to implement the main features (loading coin denominations, solving the Coin Change Problem).
    Implement helper functions for repetitive tasks (e.g., reading and parsing the coin denomination file).
    Create a main function to handle user interaction and call the appropriate functions.
Error Handling:
    Ensure the program handles potential errors, such as the coin denomination file not being found or the user providing invalid inputs.
"""
from file_handler import intput
from currency_type import currency

def menu(): # Introduces the program and then lets the user choose one of the options
    print("\n\nWelcome to this Coin Change Program, where you can convert an amount of money from many currencies into the necessary different amounts of coins.")
    while True:
        choice = intput("\nConvert(1) Exit(2)\n", 1,1)
        if choice == 1:
            currency()
        elif choice == 2:
            print("Come Back Soon!")
            break
menu()

# Parsing Coins AND Code