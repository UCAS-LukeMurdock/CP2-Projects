#Luke Murdock, Drabble but Python
import csv, datetime as dt, random as r
'💵'

def int_input(prompt, range = 0, zero = False): # Checks and solves errors in integer inputs (Has Range If Needed)
    while True:
        try: 
            response = int(input(prompt).strip())
        except ValueError:
            print("Invalid Input Type")
            continue
        if range == 0 or (response > 0 and response <= range and zero == False) or (zero == True and range >= 0 and response <= range):
            break
        else:
            print("Not In Range")
            continue
    return response

prompts = ["What does your world look like? Could you draw a map of it? Does this matter in your world?",
           "What food does your character like? Is it inspired by where they are from?",
           "Your character somehow gets rich? How? What does he do with his newfound money? Does he use it selfishly or generously?",
           "What does your character like to do as a hobby?",
           "What would be your favorite topic to write a book about?",
           ]
vocab_words = ["co·na·tion /kōˈnāSH(ə)n/ (noun) the mental faculty of purpose, desire, or will to perform an action; volition.",
             "fa·nat·i·cal /fəˈnadək(ə)l/ (adjective) filled with excessive and single-minded zeal.\n\tobsessively concerned with something.",
             "pen·sive /ˈpensiv/ (adjective) engaged in, involving, or reflecting deep or serious thought.",
             "el·o·quent /ˈeləkwənt/ (adjective) fluent or persuasive in speaking or writing.\n\tclearly expressing or indicating something.",
             "ut·ter /ˈədər/ (adjective) complete; absolute.",
           ]
want_fire = False
want_prompt = False
want_money = False
words_written_on_run = 0
signed_in = False
person_ind = int()
users = []

with open("personal/drabble_folder/streak.csv", "r") as file:
    reader = csv.reader(file)
    for row_index, row in enumerate(reader):
        if row_index == 0:
            detail_types = row
            continue
        dict = {}
        for detail_index, detail in enumerate(row):
            dict.update({detail_types[detail_index]:detail})
        users.append(dict)

def file_write(): # Writes the list of dictonary profiles onto the file
    with open ("personal/drabble_folder/streak.csv", "w", newline="") as file:
        fieldnames = ["Name","Streak","Day","Coins","Gems"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(users)

def write(): # 
    global words_written_on_run
    writing = input(f"{prompts[r.randrange(0,len(prompts))] if want_prompt == True else 'Free-Write'}:\n")
    words = writing.strip().split(" ")
    for word in words:
        if word == "":
            words.remove(word)
    word_count = len(words)
    words_written_on_run += word_count
    print(f"    Word Count: {word_count}\n")
    print("You Did The Free-Write!")
    if signed_in == True:
        streak_add()

def streak_add():
    day = str(dt.datetime.now())[:10]
    if day != users[person_ind]["Day"]:
        users[person_ind]["Streak"] = int(users[person_ind]["Streak"]) +1
        users[person_ind]["Day"] = day
        print(f"Your Streak has Increased to {users[person_ind]["Streak"]}{f'🔥' if want_fire == True else ''}!")
        file_write()

def display_prompt():
    print(f"Prompt for Writing Ideas:\n{prompts[r.randrange(0,len(prompts))]}")

def word():
    print(f"Vocabulary Word:\n{vocab_words[r.randrange(0,len(vocab_words))]}")

def streak_display(): # 
    if signed_in == True:
        fire = '🔥'*int(users[person_ind]['Streak'])
        print(f"{users[person_ind]["Name"]}'s Streak: {users[person_ind]["Streak"]}{f'\n{fire}' if want_fire == True else ''}")
    elif signed_in == False:
        print("You Aren't Signed In")

def social():
    # for user in users:
    #     print(f"Name: {user["Name"]}\nStreak: {user["Streak"]}\n")
    print("\nStreak Leaderboard")
    streaks = []
    for user in users:
        streaks.append([user["Streak"], user["Name"]])
    ranked_streaks = sorted(streaks, key=lambda user: int(user[0]), reverse=True)
    for rank, streak in enumerate(ranked_streaks[:10]):
        fire = ('🔥'*int(streak[0]))
        print(f"{rank+1}. {f'{streak[1]}-    \t' if len(streak[1]) <= 4 else f'{streak[1][:9]}|-\t' if len(streak[1]) > 9 else f'{streak[1]}-\t'}{streak[0]}{f'\t{fire}' if want_fire == True else ''}")

def settings():
    global want_fire, want_prompt, want_money
    while True:
        change = int_input(f"""
Settings
    What do you want changed? [Exit(0)]:
    Fire Emojis- {f'Activated [🔥] ' if want_fire == True else 'Deactivated'}(1)
    Write With Prompt- {'Activated' if want_prompt == True else 'Deactivated'}(2)
    Shop- {'Activated [💸] ' if want_money == True else 'Deactivated'}(3)
""", 3, zero = True)
        if change == 0:
            break
        elif change == 1:
            want_fire = not want_fire
        elif change == 2:
            want_prompt = not want_prompt
        elif change == 3:
            want_money = not want_money

def sign_in(username):
    global person_ind
    found = False
    while not found:
        if username == "0":
            break
        for user_ind, user in enumerate(users):
            if username == user["Name"]:
                found = True
                person_ind = user_ind
                print(f"Welcome {users[person_ind]["Name"]}!")
                return True
        if found == False:
            print("Couldn't Find That User")
            break

def sign_up(): #CATCH DUPLICATES!!!
    new_name = input("Username For New User: ")
    users.append({"Name":new_name, "Streak":0, "Day":0, "Coins":0, "Gems":0})
    sign_in(new_name)
    file_write()

def shop(emoji_menu):
    while True:
        print(f"{users[person_ind]["Coins"]}🟡 {users[person_ind]["Gems"]}💎")
        order = int_input(f"""Shop [Exit(0)]:
    Emoji Menu(1)- 5🟡
""",1, zero = True)
        if order == 0:
            print("Thanks for Shopping!")
            break
        elif order == 1:
            users[person_ind]["Coins"] = str(int(users[person_ind]["Coins"]) -5)
            emoji_menu = True
    return emoji_menu

def main(): # Introduces the program and then lets the user choose one of the options
    emoji_menu = False
    global signed_in
    print("\nWelcome to Drabble, where you can write every day to grow your streak.")
    while True:
        if emoji_menu == False:
            choice = int_input(f"\nWrite(1) Prompt(2) Word(3) Streak(4) Leaderboard(5) Settings(6) {'Sign In' if signed_in == False else 'Change User'}(7) {'Sign Up' if signed_in == False else 'Sign Out'}(8){' Shop(9)' if want_money == True else ''} Exit(0)\n", 9, zero = True)
        elif emoji_menu == True:
            choice = int_input(f"\nWrite📝✍️(1) Prompt❔(2) Word💬(3) Streak🔥(4) Leaderboard🏆(5) Settings⚙️(6) {'Sign In' if signed_in == False else 'Change User'}👥(7) {'Sign Up' if signed_in == False else 'Sign Out'}👤(8){' Shop💸(9)' if want_money == True else ''} Exit(0)\n", 9, zero = True)
        if choice == 1:
            write()
        elif choice == 2:
            display_prompt()
        elif choice == 3:
            word()
        elif choice == 4:
            streak_display()
        elif choice == 5:
            social()
        elif choice == 6:
            settings()
        elif choice == 7:
            if sign_in(input("Username [Exit(0)]: ")) == True:
                signed_in = True
        elif choice == 8:
            if signed_in == False:
                sign_up()
                signed_in = True
            elif signed_in == True:
                print("Successfully Signed Out")
                signed_in = False
        elif choice == 9:
            if want_money == True:
                emoji_menu = shop(emoji_menu)
            else:
                print("Not In Range")
        elif choice == 0:
            print(f"\nYou Wrote {words_written_on_run} Words!\nCome Back Soon!\n")
            break
main()

#Add Money, WPM, Shop, Fix Creation of Accounts, More Prompts and Words, Save stuff, Losing Streak