#Luke Murdock, Shop
from file_handler import read_file, write_file, intput

def shop():
    characs = read_file()
    ind = -1
    charac_name = input("What is the name of the character you want to shop as?:\n").strip()
    for charac_ind, charac in enumerate(characs):
        if charac_name.upper() == charac["Name"].upper():
            ind = charac_ind
    if ind == -1:
        print(f"\n{charac_name} Can't Be Found")
        return
    item = intput("$5 Poison(1) $5 Freeze(2) $7 Protection(3) $10 Sharp Sword(4) Exit(5)\n", 1,5)

    def cost_check(cost):
        nonlocal characs, ind
        if characs[ind]["Money"] < cost:
            print(f"{characs[ind]["Name"]} doesn't have enough Money")
            return False
        return True

    if item > 0 and item < 4:
        if characs[ind]["Potion"] != "none":
            print(f"{characs[ind]["Name"]} already has a Potion")
            return
        elif cost_check(5) == False:
            return
        elif item == 1:
            characs[ind]['Potion'] = 'Poison'
            characs[ind]['Money'] += -5
        elif item == 2:
            characs[ind]['Potion'] = 'Freeze'
            characs[ind]['Money'] += -5
        elif item == 3:
            if cost_check(7) == False:
                return
            characs[ind]['Potion'] = 'Protect'
            characs[ind]['Money'] += -7
    if item == 4:
        if characs[ind]["Sword"] == "yes":
            print(f"{characs[ind]["Name"]} already has the Sharp Sword")
            return
        elif cost_check(10) == False:
            return
        else:
            characs[ind]['Sword'] = 'yes'
            characs[ind]['Money'] += -10
    else:
        return
    write_file(characs)

def equip():
    characs = read_file()
    ind = -1
    charac_name = input("What is the name of the character you want to equip as?:\n").strip()
    for charac_ind, charac in enumerate(characs):
        if charac_name.upper() == charac["Name"].upper():
            ind = charac_ind
    if ind == -1:
        print(f"\n{charac_name} Can't Be Found")
        return
    choice = intput("Equip Basic Sword(1) Equip Sharp Sword(2)\n", 1,2)
    if choice == 1:
        characs[ind]["Equipped"] = "no"
    elif choice == 2:
        if characs[ind]["Sword"] == "no":
            print(f"{characs[ind]["Name"]} don't own Sharp Sword (Buy it in the Shop)")
            return
        else:
            characs[ind]["Equipped"] = "yes"
    write_file(characs)