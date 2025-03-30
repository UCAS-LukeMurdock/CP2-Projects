# Luke Murdock, Currency Type Handler
from file_handler import read_file
from coin_convert import convert

def currency(): # Finds out which Currency the user wants to use
    currencies = read_file()
    while True:
        found = False
        choice = input("\nWhich currency do you want to use?:\nUS Dollar(USD) Euro(EUR) British Pound Sterling(GBP) Japanese Yen(JPY) Exit(0)\n").strip().upper()
        for currency in currencies:
            if choice == currency["Abbrevi"] or choice == currency["Currency"].upper():
                found = True
                user_currency = currency
                break
        if found == True:
            convert(user_currency)
        elif choice == "0":
            print("\n\n\nCome Back Soon!\n\n\n")
            break
        else:
            print("Invalid Input: Try Again (Enter the Name, Abbreviation, or 0 [for Exit])")