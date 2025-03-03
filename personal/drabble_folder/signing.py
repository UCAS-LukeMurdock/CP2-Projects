# Luke Murdock, Signing with Accounts and Users
from file_handler import read_file as read, write_file as write

def sign_in(username, signed_in, person_ind, coins, emoji_menu, wpm, freeze, password, have_store, storage):
    users = read()
    found = False
    for user_ind, user in enumerate(users):
        if username == user["Name"]:
            found = True
            person_ind = user_ind
            coins = int(users[person_ind]["Coins"])
            emoji_menu = users[person_ind]["Bought"]["Emoji Menu"]
            wpm = users[person_ind]["Bought"]["WPM"]
            freeze = users[person_ind]["Bought"]["Freeze"]
            password = users[person_ind]["Bought"]["Password"]
            have_store = password = users[person_ind]["Bought"]["Store"]
            if have_store == True:
                storage = users[person_ind]["Storage"]
            print(f"\tWelcome, {users[person_ind]["Name"]}!")
            signed_in = True
    if found == False:
        print("Couldn't Find That User")
    return signed_in, person_ind, coins, emoji_menu, wpm, freeze, password, have_store, storage

def sign_up(signed_in, person_ind, coins, emoji_menu, wpm, freeze, password, have_store, storage): #CATCH DUPLICATES!!!  NO 0 as New Name!
    users = read()
    new_name = input("Username For New User: ")
    users.append({"Name":new_name,
                  "Streak":0,
                  "Day":0,
                  "Coins":0,
                  "Gems":0,
                  "Bought": {"Emoji Kitchen":False,"WPM":False,"Freeze":False,"Password":False,"Store":False},
                  "Storage": ''
                  })
    write(users)
    return sign_in(new_name, signed_in, person_ind, coins, emoji_menu, wpm, freeze, password, have_store, storage)