# Luke Murdock, Financial Calculator

def main():
    while True:
        try:
            choice = int(input("Financial Calculator:\nBudget(1) Tip(2) Sale Price(3) Compoud Interest(4) Goal End(5) Done(6)\n"))        
        except:
            print("Invalid Input")
            continue
        if choice <= 0 or choice > 6:
            print("Invalid Input")
            continue
        break

    if choice == 1:
        budget()
    elif choice == 2:
        tip()
    elif choice == 3:
        sale()
    elif choice == 4:
        comp()
    elif choice == 5:
        goal()
    elif choice == 6:
        print("Come back soon!")
        return
    
def budget():
    while True:
        try:
            ans = float(input("How much money do you have?: "))
        except:
            print("Invalid Input")
            continue
        break
    # Formats and calculates how much money should be spent in each category
    print(f"Savings: ${round(ans*0.2, 2):,.2f} Bills: ${round(ans*0.5, 2):,.2f}")
    print(f"Food: ${round(ans*0.2, 2):,.2f}")
    print(f"Fun: ${round(ans*0.1, 2):,.2f}")
    main()
def tip():
    while True:
        try:
            cost = float(input("How much are you spending?: "))
            tip = float(input("What percentage is your tip in decimal form?: "))
        except:
            print("Invalid Input")
            continue
        break
    
    print(f"Tip Cost: ${round(cost*tip, 2):,.2f} Total Cost: ${round(cost*tip+cost, 2):,.2f}")
def sale():
    while True:
        try:
            cost = float(input("How much are you spending?: "))
            disc = float(input("What percentage is your discount in decimal form?: "))
        except:
            print("Invalid Input")
            continue
        break
    print(f" ${round(, 2):,.2f}")
def comp():
    pass
def goal():
    pass

main()

# ${round(, 2):,.2f}
while True:
    try:
        a = float(input("How much are you spending?: "))
    except:
        print("Invalid Input")
        continue
        break

#
#