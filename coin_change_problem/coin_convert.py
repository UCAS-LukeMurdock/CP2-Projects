# Luke Murdock, Converts Amount into Coins

def convert(currency): # Finds out which and how many coins/denominations are needed for the inputted amount of money for the previously inputted currency (Solves the Coin Change Problem)
    found = False
    try:
        if currency["Abbrevi"] != "JPY":
            amount = int(round(float(input("How much money are you putting in?:\n")),2) * 100)
        else:
            amount = int(round(float(input("How much money are you putting in?:\n"))) * 100)
    except:
        print("Invalid Input: Try Again (Insert a Number)")
        return
    print("\nResults:")

    def decide_denomin(denomin): # Decides if the certain denomination is needed and how much for the user's inputted amount
        nonlocal found,amount
        denomin = denomin.split("-")
        denomin[1] = int(denomin[1])

        quotient = amount / denomin[1]
        not_remain = amount // denomin[1]

        if quotient > 0 and quotient >= 1:
            found = True
            print(f"{not_remain} {denomin[0]}{'s' if not_remain > 1 else ''}")
            amount -= not_remain*denomin[1]

    for denomin in currency["Denomin"]:
        decide_denomin(denomin)
    if found == False:
        print("None")