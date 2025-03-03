#Luke Murdock, Main
from file_handler import int_input
from writing import free_write, display_prompt, word, streak_check
from streaks_file import streak_display, social
from settings import settings
from signing import sign_in, sign_up
from shop import shop
'💵'

def menu(): # Introduces the program and then lets the user choose one of the options
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

    emoji_menu = False
    wpm = False

    freeze = False
    password = False
    have_store = False
    storage = ""

    coins = 0
    words_written_on_run = 0
    signed_in = False
    person_ind = int()

    print("\nWelcome to Drabble, where you can write every day to grow your streak.")
    while True:
        if emoji_menu == False:
            choice = int_input(f"\nWrite(1) Prompt(2) Word(3) Streak(4) Leaderboard(5) Settings(6) {'Sign In' if signed_in == False else 'Change User'}(7) {'Sign Up' if signed_in == False else 'Sign Out'}(8){' Shop(9)' if want_money == True else ''} Exit(0)\n", 9, zero = True)
        elif emoji_menu == True:
            choice = int_input(f"\nWrite📝✍️ (1) Prompt❔(2) Word💬(3) Streak🔥(4) Leaderboard🏆(5) Settings ⚙️ (6) {'Sign In' if signed_in == False else 'Change User'}👥(7) {'Sign Up' if signed_in == False else 'Sign Out'}👤(8){' Shop💸(9)' if want_money == True else ''} Exit(0)\n", 9, zero = True)
        if choice == 1:
            words_written_on_run += free_write(signed_in, prompts, vocab_words, want_prompt, person_ind, want_fire)
        elif choice == 2:
            display_prompt(prompts)
        elif choice == 3:
            word(vocab_words)
        elif choice == 4:
            streak_display(signed_in, person_ind, want_fire)
        elif choice == 5:
            social(want_fire)
        elif choice == 6:
            want_fire, want_prompt, want_money = settings(want_fire, want_prompt, want_money)
        elif choice == 7:
            signed_in, person_ind, coins, emoji_menu, wpm, freeze, password, have_store, storage = sign_in(input("Username [Exit(0)]: "), signed_in, person_ind, coins, emoji_menu, wpm, freeze, password, have_store, storage)
            streak_check()
        elif choice == 8:
            if signed_in == False:
                signed_in, person_ind, coins, emoji_menu, wpm, freeze, password, have_store, storage = sign_up(signed_in, person_ind, coins, emoji_menu, wpm, freeze, password, have_store, storage)
                signed_in = True
            elif signed_in == True:
                print("Successfully Signed Out")
                signed_in = False
        elif choice == 9:
            if want_money == True:
                coins, emoji_menu, wpm, freeze, password, have_store = shop(signed_in,person_ind, coins, emoji_menu, wpm, freeze, password, have_store)
            else:
                print("Not In Range")
        elif choice == 0:
            print(f"\nYou Wrote {words_written_on_run} Words!\nCome Back Soon!\n")
            break
menu()

#Add Money (Challenges), WPM, Fix and Add to Shop, Fix Creation of Accounts, Save stuff, Losing Streak, More Prompts and Words, 

'''
Bought
["Emoji Menu", "WPM", "Freeze", "Password", "Storage"]
'''