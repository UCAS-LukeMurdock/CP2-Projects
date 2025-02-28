#Luke Murdock, Group 2 Code
import csv

# some_profiles = [
#     {
#         "Name": "Bob",
#         "React Scores": 5,
#         "Box Scores": 7 ,
#         "Guess Scores": 0,
#         "Genre": "Adventure",
#     },
#     {
#         "Name": "Joe",
#         "React Scores": 3,
#         "Box Scores": 6,
#         "Guess Scores": 9,
#         "Genre": "Roguelike",
#     }
# ]

profiles = []
#
with open("Scores.csv", "r") as file:
    reader = csv.reader(file)
    for row_index, row in enumerate(reader):
        if row_index == 0:
            detail_types = row
            continue
        profile = {}
        for detail_index, detail in enumerate(row):
            if detail_index == 1 or detail_index == 2 or detail_index == 3:
                detail = int(detail)
            profile.update({detail_types[detail_index]:detail})
        profiles.append(profile)

def write(): # 
    with open ("Group2 Code/scores.csv", "w", newline="") as file:
        fieldnames = ["Name","React Score","Box Score","Guess Score","Genre"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(profiles)

def int_input(prompt, range = 0): # Checks and solves errors in integer inputs (Has Range If Needed)
    while True:
        try: 
            response = int(input(prompt).strip())
        except ValueError:
            print("Invalid Input Type")
            continue
        if range == 0 or (response > 0 and response <= range):
            break
        else:
            print("Not In Range")
            continue
    return response

# VINCENT'S CODE -----------------------------------------------------------------------------------------------

# LUKE'S CODE --------------------------------------------------------------------------------------------------
def add(score, game_name): # Finds out what to add
    while True:
        found = False
        name = input("What is your username?: ").strip()
        for profile_ind, profile in enumerate(profiles):
            if name == profile["Name"]:
                found = True
                found_ind = profile_ind
                break
        if found == False:
            choice = int_input("Couldn't Find Profile\nTry Again(1) Create Profile(2)\n", 2)
            if choice == 1:
                continue
            if choice == 2:
                add_profile(name)
                print("Added Your Profile!")
                found_ind = -1
                break
        elif found == True:
            print("Found Your Profile!")
            break
    if score > profiles[found_ind][f"{game_name} Scores"]:
        profiles[found_ind][f"{game_name} Scores"] = score
        print("Successfully Added Your New Highest Score!")
    elif score <= profiles[found_ind][f"{game_name} Scores"]:
        print("You did not score higher than your highest score, so your score wasn't added")
    write()

def add_profile(name):
    genre = input("What is your favorite game genre?: ").strip()
    new_profile = {
        "Name": name, 
        "React Score": 0,
        "Box Score": 0,
        "Guess Score": 0,
        "Genre": genre
    }
    profiles.append(new_profile)


def display_profiles():
    print("Profiles:")
    for profile in profiles:
        print(f"\nUsername- {profile["Name"]}\nReaction Game Scores- {profile["React Score"]}\nReaction Box Game Scores- {profile["Box Score"]}\nNumber Guessing Game Scores- {profile["Guess Score"]}\nFavorite Genre- {profile["Genre"]}\n")

# FAIRUS'S CODE ------------------------------------------------------------------------------------------------
    


def main(): # Introduces the program and then lets the user choose one of the options
    print("Welcome to this game program, it has two different games and keeps tracks of scores and user profiles")
    while True:
        choice = int_input("\nGames(1) Scores(2) Profiles(3) Exit(4)\n", 4)
        if choice == 1:
            add(12, "React")
        elif choice == 2:
            scores()
        elif choice == 3:
            display_profiles()
        elif choice == 4:
            print("Come Back Soon!")
            break
        else:
            print("Something Broke")
            continue

main()


def add_score(score, game_name): # Adds the user's new score to their profile if they have its pasword or else it lets them create a new profile
    profiles = read_file()
    while True:
        found = False
        redo = False
        name = input("What is your username? (Type 0 if you don't have one):\n").strip().upper()
        for profile_ind, profile in enumerate(profiles):
            if name == profile["Name"].upper():
                found = True
                found_ind = profile_ind
                print("Found Profile!")
                if score <= profiles[found_ind][f"{game_name} Score"]:
                    break
                password = input("Type Your Password:\n").strip().upper()
                if password == profile["Password"].upper():
                    break
                else:
                    redo = True
                    print("That is not the correct password for this profile. Try Again")
                    break
        if found == False:
            choice = create_profile_choice()
            if choice == 1:
                continue
            elif choice == 2:
                profiles.append(add_profile())
                print("Added Your Profile!")
                found_ind = -1
                break
        elif found == True and redo == False:
            break
        else:
            continue
    if score > profiles[found_ind][f"{game_name} Score"]:
        profiles[found_ind][f"{game_name} Score"] = score
        print("Successfully Added Your New Highest Score!")
    elif score <= profiles[found_ind][f"{game_name} Score"]:
        print("You did not score higher than your highest score, so your score wasn't added\n")
    write(profiles)





def add_score(score, game_name): # Adds the user's new score to their profile if they have its pasword or else it lets them create a new profile
    profiles = read_file()
    while True:
        found = False
        name = input("What is your username?: ").strip().upper()
        for profile_ind, profile in enumerate(profiles):
            if name == profile["Name"].upper():
                found = True
                found_ind = profile_ind
                password = input("Found Your Profile!\nType Your Password:\n").strip().upper()
                if password == profile["Password"].upper():
                    break
                else:
                    print("That is not the correct password for this profile. Try Again")
                    continue
        if found == False:
            choice = create_profile_choice()
            if choice == 1:
                continue
            elif choice == 2:
                profiles.append(add_profile(score, game_name))
                print("Added Your Profile!")
                found_ind = -1
                break
        elif found == True:
            break
    if score > profiles[found_ind][f"{game_name} Score"]:
        profiles[found_ind][f"{game_name} Score"] = score
        print("Successfully Added Your New Highest Score!")
    elif score <= profiles[found_ind][f"{game_name} Score"]:
        print("You did not score higher than your highest score, so your score wasn't added\n")
    write(profiles)

















    #Luke Murdock, Adding Scores
import csv

def read_file(): # Turns a file into a list of dictionary profiles
    profiles = []
    with open("Scores.csv", "r") as file:
        reader = csv.reader(file)
        for row_index, row in enumerate(reader):
            if row_index == 0:
                detail_types = row
                continue
            profile = {}
            for detail_index, detail in enumerate(row):
                if detail_index == 2 or detail_index == 3 or detail_index == 4:
                    detail = int(detail)
                profile.update({detail_types[detail_index]:detail})
            profiles.append(profile)
    return profiles

def write(profiles): # Writes the list of dictonary profiles onto the file
    with open ("Scores.csv", "w", newline="") as file:
        fieldnames = ["Password","Name","React Score","Box Score","Guess Score","Genre"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(profiles)

def add_profile(): # Creates a new profile and puts it onto the list of profiles
    name = input("What is your username for your new profile?:\n").strip()
    password = input("What is your password for your new profile?:\n").strip()
    genre = input("What is your favorite game genre?:\n").strip()
    new_profile = {
        "Password": password,
        "Name": name,
        "React Score": 0,
        "Box Score": 0,
        "Guess Score": 0,
        "Genre": genre }
    return new_profile

def create_profile_choice(): # Lets the user decide if they want to create a new profile or try to find their profile again
    while True:
        try:
            choice = int(input("Couldn't Find Profile\nTry Again(1) Create Profile(2)\n").strip())
        except:
            print("Invalid Input Type")
            continue
        if choice <= 0 or choice > 2:
            print("Not In Range")
            continue
        elif choice > 0 or choice <= 2:
            return choice

def add_score(score, game_name): # Adds the user's new score to their profile if they have its pasword or else it lets them create a new profile
    profiles = read_file()
    while True:
        found = False
        redo = False
        name = input("What is your username? (Type 0 if you don't have one):\n").strip().upper()
        for profile_ind, profile in enumerate(profiles):
            if name == profile["Name"].upper():
                found = True
                found_ind = profile_ind
                print("Found Profile!")
                if score <= profiles[found_ind][f"{game_name} Score"]:
                    break
                password = input("Type Your Password:\n").strip().upper()
                if password == profile["Password"].upper():
                    break
                else:
                    redo = True
                    print("That is not the correct password for this profile. Try Again")
                    break
        if found == False:
            choice = create_profile_choice()
            if choice == 1:
                continue
            elif choice == 2:
                profiles.append(add_profile())
                print("Added Your Profile!")
                found_ind = -1
                break
        elif found == True and redo == False:
            break
        else:
            continue
    if score > profiles[found_ind][f"{game_name} Score"]:
        profiles[found_ind][f"{game_name} Score"] = score
        print("Successfully Added Your New Highest Score!")
    elif score <= profiles[found_ind][f"{game_name} Score"]:
        print("You did not score higher than your highest score, so your score wasn't added\n")
    write(profiles)