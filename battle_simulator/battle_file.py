# Luke Murdock, Managing Battles
from file_handler import read_file, write_file, intput
import random

def who():
    characs = read_file()
    fighter, opponent = {}, {}
    fighter_name = input("What is the name of the character you want to fight as?:\n")
    opponent_name = input("What is the name of the character you want to fight?:\n")
    for charac in characs:
        if fighter_name == charac["Name"]:
            fighter = charac
        elif opponent_name == charac["Name"]:
            opponent = charac
    if fighter == {} or opponent == {}:
        print("At Least One of Those Characters Can't Be Found\n")
        fighter, opponent = who()
    return fighter, opponent

def battle():
    fighter, opponent = who()
    user_hp = 10 * int(fighter["Health"])
    op_hp = 10 * int(opponent["Health"])
    while user_hp <= 0 or op_hp <= 0:
                # def status():
                #     nonlocal fighter, user_hp, opponent, op_hp
                #     print(f"{fighter['Name']}'s HP: {user_hp}   {opponent['Name']}'s HP: {op_hp}")
                # status()
        print(f"{fighter['Name']}'s HP: {user_hp}   {opponent['Name']}'s HP: {op_hp}")
        # Action
        def actions(action):
            if action == 6:
                user_hp = 0
                return #HHHHOOOWWWWW!!!!!
            elif action == 1:
                pass
            elif action == 2:
                pass
            elif action == 3:
                pass
            elif action == 4:
                pass
            elif action == 5:
                pass
        actions(intput("Attack(1) Defend(2) Dodge(3) Heal(4) Class Power(5) Give Up(6)", 1,6))

        # Op Action
        actions(random.randint(1,5))

    characs = read_file()
    if user_hp <= 0:
        print("You Lost")
    elif op_hp <= 0:
        print("You Won!")
        characs[fighter]["Level"] += 1
    write_file(characs)