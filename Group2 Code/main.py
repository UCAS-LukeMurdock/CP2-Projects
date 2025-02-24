#Luke Murdock, Group 2 Code
import csv

# some_profiles = [
#     {
#         "Name": "Bob",
#         "React Scores": [1,2,5],
#         "Box Scores": [1,2,5],
#         "Guess Scores": [1,2,5],
#         "Genre": "Adventure",
#     },
#     {
#         "Name": "Joe",
#         "React Scores": [1,2,5],
#         "Box Scores": [1,2,5],
#         "Guess Scores": [1,2,5],
#         "Genre": "Roguelike",
#     }
# ]

profiles = []
#
with open("Group2 Code/scores.csv", "r") as file:
    reader = csv.reader(file)
    for row_index, row in enumerate(reader):
        if row_index == 0:
            detail_types = row
            continue
        profile = {}
        for detail_index, detail in enumerate(row):
            if detail_index == 1 or detail_index == 2 or detail_index == 3:
                detail = eval(detail)
                # detail = detail[1:-1].split(",") # This commented code doesn't work for short lists
                # for char_ind, char in enumerate(detail):
                #     detail[char_ind] = int(char.strip())
            profile.update({detail_types[detail_index]:detail})
        profiles.append(profile)

def write(): # 
    with open ("Group2 Code/scores.csv", "w", newline="") as file:
        fieldnames = ["Name","React Scores","Box Scores","Guess Scores","Genre"]
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
def add(score, game): # Finds out what to add
    found = False
    name = input("What is your username?: ").strip()
    for profile_ind, profile in enumerate(profiles):
        if name == profile["Name"]:
            found = True
            found_ind = profile_ind
            break
    if found == False:
        choice = int_input("Couldn't Find Profile. Try Again(1) Create Profile(2)", 2)
        if choice == 
        add_profile(name)
        print("Added Your Profile!")
        found_ind = -1
    elif found == True:
        print("Found Your Profile!")
    
    profiles[found_ind][f"{game} Scores"].append(score)
    print("Successfully Added The Score!")
    write()

def add_profile(name):
    genre = input("What is your favorite game genre?: ").strip()
    new_profile = {
        "Name": name, 
        "React Scores": [], 
        "Box Scores": [], 
        "Guess Scores": [], 
        "Genre": genre
    }
    profiles.append(new_profile)


def display_profiles():
    print("Profiles:")
    for profile in profiles:
        print(f"\nUsername- {profile["Name"]}\nReaction Game Scores- {profile["React Scores"]}\nReaction Box Game Scores- {profile["Box Scores"]}\nNumber Guessing Game Scores- {profile["Guess Scores"]}\nFavorite Genre- {profile["Genre"]}\n")

# FAIRUS'S CODE ------------------------------------------------------------------------------------------------
    


def main(): # Introduces the program and then lets the user choose one of the options
    print("Welcome to this game program, it has two different games and keeps tracks of scores and user profiles")
    while True:
        choice = int_input("\nGames(1) Scores(2) Profiles(3) Exit(4)\n", 4)
        if choice == 1:
            add(10, "React")
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