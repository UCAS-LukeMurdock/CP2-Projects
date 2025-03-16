# Luke Murdock, Character Handler
from file_handler import read_file, write_file, intput

def class_stats(user_class, charac):
    if user_class == 1:
        charac["Class"] = "Basic Human"
        charac["Health"] += 1
        charac["Strength"] += 1
        charac["Defense"] += 1
        charac["Speed"] += 1
    elif user_class == 2:
        charac["Class"] = "Knight"
        charac["Health"] += 1
        charac["Strength"] += 2
        charac["Defense"] += 1
        charac["Speed"] += -1
    elif user_class == 3:
        charac["Class"] = "Ranger"
        charac["Strength"] += 2
        charac["Defense"] += -1
        charac["Speed"] += 2
    elif user_class == 4:
        charac["Class"] = "Mage"
        charac["Health"] += 2
        charac["Strength"] += -1
        charac["Speed"] += 2
    return charac

def create():
    points_left = 16
    name = input("\nCharacter's Name: ").strip()
    user_class = intput("\nCharacter's Class (Classes Affect Stats and Powers):\nBasic Human(1) Knight(2) Ranger(3) Mage(4)\n", 1,4)
    print("\nYour character has four stats: Health, Strength, Defense, Speed\nThey are given 16 points overall and you decide how many points are allocated to each stat")
    def stat_input(stat_type):
        nonlocal points_left
        stat = intput(f"Character's {stat_type} Stat: ", 0,points_left)
        points_left -= stat
        return stat
    health = stat_input("Health")
    stren = stat_input("Strength")
    defen = stat_input("Defense")
    speed = stat_input("Speed")
    charac = {
        "Name": name,
        "Class": "Added Soon",
        "Level": 0,
        "Health": health,
        "Strength": stren,
        "Defense": defen,
        "Speed": speed,
        "Money": 0,
        "Potion": "none",
        "Sword": "no",
        "Equipped": "no"}
    charac = class_stats(user_class, charac)
    print("\nApplied Class Stat Changes\n")
    print(f"Character Created\n{charac["Name"]}:\nClass- {charac["Class"]}\nLevel- {charac["Level"]}\nMoney- ${charac["Money"]}\nHealth Stat- {charac["Health"]}\nStrength Stat- {charac["Strength"]}\nDefense Stat- {charac["Defense"]}\nSpeed Stat- {charac["Speed"]}\nPotion- {charac["Potion"]}\nSword- {'Basic' if charac["Sword"] == 'no' else 'Sharp' if charac["Equipped"] == 'yes' else 'Basic (Sharp Unequipped)'}")
    retry = intput(f"\nYou Have {points_left} points left\nRetry(1) Keep(2)\n", 1,2)
    if retry == 1:
        create()
        return
    characs = read_file()
    characs.append(charac)
    write_file(characs)

def display():
    characs = read_file()
    print("\nYour Characters")
    if characs == []:
        print("\nNone")
        return
    for charac in characs:
        print(f"\n{charac["Name"]}:\nClass- {charac["Class"]}\nLevel- {charac["Level"]}\nMoney- ${charac["Money"]}\nHealth Stat- {charac["Health"]}\nStrength Stat- {charac["Strength"]}\nDefense Stat- {charac["Defense"]}\nSpeed Stat- {charac["Speed"]}\nPotion- {charac["Potion"]}\nSword- {'Basic' if charac["Sword"] == 'no' else 'Sharp' if charac["Equipped"] == 'yes' else 'Basic (Sharp Unequipped)'}")

def remove():
    characs = read_file()
    name = input("What is the name of the character you want removed?:\n").strip()
    removed = False
    for charac in characs:
        if name.upper() == charac["Name"].upper():
            characs.remove(charac)
            removed = True
            print("Successfully Removed")
            write_file(characs)
            return
    print("Unsuccessfully Removed")
