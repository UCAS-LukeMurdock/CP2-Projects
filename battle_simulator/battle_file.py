# Luke Murdock, Managing Battles
from file_handler import read_file, write_file, intput
import random

def level_up(characs, ind):
    stat = intput("You Leveled Up!\nChoose Which Stat to be Improved\nHealth(1) Strength(2) Defense(3) Speed(4)\n", 1,4)
    if stat == 1:
        characs[ind]["Health"] += 1
    elif stat == 2:
        characs[ind]["Strength"] += 1
    elif stat == 3:
        characs[ind]["Defense"] += 1
    elif stat == 4:
        characs[ind]["Speed"] += 1
    return characs

def who():
    characs = read_file()
    fighter, opponent = {}, {}
    fighter_name = input("What is the name of the character you want to fight as? [Exit(0)]:\n").strip()
    if fighter_name == "0":
        return False, False, False
    opponent_name = input("What is the name of the character you want to fight?:\n").strip()
    for charac_ind, charac in enumerate(characs):
        if fighter_name.upper() == charac["Name"].upper():
            fighter, fighter_ind = charac, charac_ind
        elif opponent_name.upper() == charac["Name"].upper():
            opponent = charac
    if fighter == {} or opponent == {}:
        print("\nAt Least One of Those Characters Can't Be Found")
        fighter, fighter_ind, opponent = who()
    return fighter, fighter_ind, opponent

def battle():
    characs = read_file()
    fighter, fighter_ind, opponent = who()
    if fighter == False:
        return
    user_hp = 10 * fighter["Health"]
    op_hp = 10 * opponent["Health"]
    # Default Statuses
    user_poison, user_poison_count, user_frozen, user_frozen_count, user_protect, user_protect_count, user_protected_hp, gave_up = False,4,False,2,False,3,0,False
    op_poison, op_poison_count, op_frozen, op_frozen_count, op_protect, op_protect_count, op_protected_hp, = False,4,False,2,False,3,0
    while user_hp > 0 and op_hp > 0:
        print(f"{fighter['Name']}'s (Your) HP: {user_hp}     {opponent['Name']}'s (Opponent's) HP: {op_hp}\n")
        user_action = intput("Attack(1) Defend(2) Dodge(3) Heal(4) Class Power(5) Potion(6) Give Up(7)\n", 1,7)
        if user_action == 7:
            user_hp = 0
            gave_up = True
            return
        if opponent["Potion"] == 'none':
            op_action = random.randint(1,5)
        else:
            op_action = random.randint(1,6)

        def turn(attacker, attacker_action, defender, defender_action, defender_hp):
            attack, poison, frozen, protect = 0,False,False,False
            if defender_action == 2 and random.randint(1,10-defender["Speed"]) == 1:
                print(f"{defender["Name"]} Dodged!")
            elif defender_action != 2 and attacker_action == 1:
                if attacker_action == 1 and defender_action != 2:
                    attack = attacker["Strength"] - defender["Defense"]//6
                elif attacker_action == 1 and defender_action == 2:
                    attack = attacker["Strength"] - defender["Defense"]//3 *2
                print(f"{attacker["Name"]} Hit {defender["Name"]}{f' But {defender["Name"]} was in a Defense Stance' if defender_action == 2 else ''}!")
            if defender_action == 4:
                defender_hp += defender["Health"]//4
                print(f"{defender["Name"]} Successfully Healed!")
            elif attacker_action == 5:
                if attacker["Class"] == "Basic Human":
                    print(f"{attacker["Name"]} Can't Use a Class Power since they are a Basic Human")
                elif attacker["Class"] == "Knight":
                    if defender_action != 3:
                        attack = attacker["Strength"] 
                        print(f"{attacker["Name"]} used Thrust on {defender["Name"]}!")
                    else:
                        print(f"{attacker["Name"]} used Thrust but {defender["Name"]} Dodged!")
                elif attacker["Class"] == "Ranger":
                    attack = attacker["Strength"] + attacker["Speed"] - defender["Defense"]
                    print(f"{attacker["Name"]} Shot {defender["Name"]}!")
                elif attacker["Class"] == "Mage":
                    if defender_action != 3:
                        defender_hp -= attacker["Health"]*2 - defender["Defense"]//2*3
                        print(f"{attacker["Name"]} Blasted {defender["Name"]}!")
                    else:
                        print(f"{attacker["Name"]} used Blast but {defender["Name"]} Dodged!")
            elif attacker_action == 6:
                if attacker["Potion"] == "none":
                    print(f"{attacker["Name"]} doesn't have any Potions")
                else:
                    if attacker["Potion"] == "Poison":
                        print(f"{attacker["Name"]} Poisoned {defender["Name"]}!")
                        poison = True
                    elif attacker["Potion"] == "Frozen":
                        print(f"{attacker["Name"]} Froze {defender["Name"]}!")
                        frozen = True
                    elif attacker["Potion"] == "Protect":
                        print(f"{attacker["Name"]} used Protection!")
                        protect = True
            if attack > 0:
                if attacker_action == 5 and attacker["Class"] == "Ranger":
                    defender_hp -= attack
                else:
                    if attacker["Equipped"] == "no":
                        defender_hp -= attack
                    else:
                        defender_hp -= attack + 5
            return defender_hp, poison, frozen, protect
        
        if user_frozen_count < 2:
            print(f"{opponent["Name"]} is still Frozen!")
            user_frozen_count += 1
            if user_frozen_count == 2:
                    print(f"{opponent["Name"]} has unfroze!")
        else:
            user_hp, op_poison, op_frozen, op_protect = turn(opponent, op_action, fighter, user_action, user_hp)
            if op_poison == True:
                op_poison_count = 0
                opponent["Potion"] = 'none'
            elif op_frozen == True:
                op_frozen_count = 0
                opponent["Potion"] = 'none'
            elif op_protect == True:
                op_protect_count = 0
                op_protected_hp = op_hp
                opponent["Potion"] = 'none'
            if user_poison_count < 4:
                print(f"{opponent["Name"]} felt the poison!")
                op_hp -= 3
                user_poison_count += 1
                if user_poison_count == 4:
                    print(f"{opponent["Name"]} has finally recovered from the poison!")
            if user_protect_count < 3:
                print(f"All damage {fighter["Name"]} recieved was negated because they were protected")
                user_hp = user_protected_hp
                user_protect_count += 1
        if op_frozen_count < 2:
            print(f"{fighter["Name"]} is still Frozen!")
            op_frozen_count += 1
            if op_frozen_count == 2:
                    print(f"{fighter["Name"]} has unfroze!")
        else:
            op_hp, user_poison, user_frozen, user_protect = turn(fighter, user_action, opponent, op_action, op_hp)
            if user_poison == True:
                user_poison_count = 0
                characs[fighter_ind]["Potion"] = 'none'
            elif user_frozen == True:
                user_frozen_count = 0
                characs[fighter_ind]["Potion"] = 'none'
            if user_protect == True:
                user_protect_count = 0
                user_protected_hp = user_hp
                characs[fighter_ind]["Potion"] = 'none'
            if op_poison_count < 4:
                print(f"{fighter["Name"]} felt the poison!")
                user_hp -= 3
                op_poison_count += 1
                if op_poison_count == 4:
                    print(f"{fighter["Name"]} has finally recovered from the poison!")
            if op_protect_count < 3:
                print(f"All damage {opponent["Name"]} recieved was negated because they were protected")
                op_hp = op_protected_hp
                op_protect_count += 1

    if user_hp <= 0:
        print("\nYou Lost")
        if gave_up == False:
            characs[fighter_ind]["Money"] += 1
    elif op_hp <= 0:
        print("\nYou Won!")
        characs[fighter_ind]["Money"] += 2
        characs[fighter_ind]["Level"] += 1
        characs = level_up(characs, fighter_ind)
    write_file(characs)