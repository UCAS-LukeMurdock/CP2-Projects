# Luke Murdock, Shop
from file_handler import read_file as read, write_file as write, int_input

def shop(signed_in,person_ind, coins, emoji_menu, wpm, freeze, password, have_store):
    users = read()
    cost = 0
    while True:
        shop_type = int_input(f"Which Shop? [Exit(0)]: Your Coins- {coins}🟡(1) Your Gems- {users[person_ind]["Gems"]}💎(2)\n", 2, zero = True)
        if shop_type == 0:
            return coins, emoji_menu, wpm, freeze, password, have_store
        if shop_type == 2 and signed_in == False:
            print("You Are Not Signed In")
            continue
        while True:
            order = int_input(f"""Shop [Exit(0)]:
    {f"Emoji Menu(1)- {'5🟡' if shop_type == 1 else '5💎'}" if emoji_menu == False else'Bought'}
    {f"WPM(2)- {'20🟡' if shop_type == 1 else '20💎'}" if wpm == False else'Bought'}
    {f"{'Charcoal Pen(3)- 30💎' if shop_type == 2 else 'Only Gem Shop'}" if freeze == False else'Bought'}
    {f"{'Password Protection(4)- 40💎' if shop_type == 2 else 'Only Gem Shop'}" if password == False else'Bought'}
    {f"{'Free-Write Storage(5)- 50💎' if shop_type == 2 else 'Only Gem Shop'}" if have_store == False else'Bought'}
""",5, zero = True)
            if order == 0:
                if signed_in == True:
                    write(users)
                print("Thanks for Shopping!")
                break
            elif order == 1:
                cost = 5
                if coins < cost:
                    print("You Don't Have Enough Money\n")
                elif shop_type == 1:
                    emoji_menu = True
                    coins -= cost
                    users[person_ind]["Coins"] = str(int(users[person_ind]["Coins"]) -cost)
                elif shop_type == 2:
                    emoji_menu = True
                    users[person_ind]["Bought"]["Emoji Menu"] = True
                    users[person_ind]["Gems"] = str(int(users[person_ind]["Gems"]) -cost)
            elif order == 2:
                cost = 20
                if coins < cost:
                    print("You Don't Have Enough Money\n")
                elif shop_type == 1:
                    wpm = True
                    coins -= cost
                    users[person_ind]["Coins"] = str(int(users[person_ind]["Coins"]) -cost)
                elif shop_type == 2:
                    wpm = True
                    users[person_ind]["Bought"]["WPM"] = True
                    users[person_ind]["Gems"] = str(int(users[person_ind]["Gems"]) -cost)
            elif order == 3 and shop_type == 2:
                cost = 30
                if coins < cost:
                    print("You Don't Have Enough Money\n")
                elif coins >= cost:
                    freeze = True
                    users[person_ind]["Bought"]["Freeze"] = True
                    users[person_ind]["Gems"] = str(int(users[person_ind]["Gems"]) -cost)
            elif order == 4 and shop_type == 2:
                cost = 40
                if coins < cost:
                    print("You Don't Have Enough Money\n")
                elif coins >= cost:
                    password = input("What is your password?: ")
                    users[person_ind]["Bought"]["Password"] = password
                    users[person_ind]["Gems"] = str(int(users[person_ind]["Gems"]) -cost)
            elif order == 5 and shop_type == 2:
                cost = 50
                if coins < cost:
                    print("You Don't Have Enough Money\n")
                elif coins >= cost:
                    have_store = True
                    users[person_ind]["Bought"]["Store"] = True
                    users[person_ind]["Gems"] = str(int(users[person_ind]["Gems"]) -cost)