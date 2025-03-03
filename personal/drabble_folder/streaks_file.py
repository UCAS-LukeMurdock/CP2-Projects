# Luke Murdock, Streaks and Leaderboard
from file_handler import read_file as read

def streak_display(signed_in, person_ind, want_fire): # 
    users = read()
    if signed_in == True:
        fire = '🔥'*int(users[person_ind]['Streak'])
        print(f"{users[person_ind]["Name"]}'s Streak: {users[person_ind]["Streak"]}{f'\n{fire}' if want_fire == True else ''}")
    elif signed_in == False:
        print("You Aren't Signed In")

def social(want_fire):
    users = read()
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