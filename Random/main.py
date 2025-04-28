#Luke Murdock, Random Tests

# import matplotlib.pyplot as plt
# import numpy as np
# import datetime as dt
# from faker import Faker


def log_in(name, password): # Checks to see if the user's inputted account exists
    accs = load_all()
    for acc in accs:
        if acc.name == name and acc.pasword == password:
            return True
    return False


# Luke's dislocated Functions
import matplotlib.pyplot as plt

def accuracy_visual(correct, questions): # Displays a pie chart for the accuracy of an amount of questions with an amount of correctly answered ones
    
    correct_perc = round((int(correct) / int(questions)) * 100)
    data = [100-correct_perc, correct_perc] # Add up to 100
    labels = ['Incorrect', 'Correct']
    colors = ['tab:red', 'tab:green']
    explode = (0.1, 0)

    plt.pie(data, labels=labels, colors=colors, explode=explode, shadow=True, autopct='%1.0f%%')
    plt.title('Accuracy')
    plt.show()

def do_unit(): # 
    acc = load(name) #?
    # Get user's account info from csv file
    #if acc.unit == final quiz
    #     Set the quiz to have every question in its question bank
    # else:
    #     if user.unit ==  on and set the lesson and quiz for that unit
    #     # input(f"The lesson content:\n{}\nPress Enter to Continue\n")
    # lesson/quiz()

def social():
    accs = load_all()
    print("\nStreak Leaderboard\n")
    streaks = []
    for acc in accs:
        streaks.append([acc.streak, acc.name])
    ranked_streaks = sorted(streaks, key=lambda acc: int(acc[0]), reverse=True)
    for rank, streak in enumerate(ranked_streaks[:10]):
        print(f"{rank+1}. {streak[1]} - {streak[0]} days")



# def social():
#     accs = [["Luke",5],["Rock", 7],["Cat",0]]
#     print("\nStreak Leaderboard")
#     streaks = []
#     for acc in accs:
#         streaks.append([acc[1], acc[0]])
#     ranked_streaks = sorted(streaks, key=lambda acc: int(acc[0]), reverse=True)
#     for rank, streak in enumerate(ranked_streaks[:10]):
#         print(f"{rank+1}. {streak[1]} - {streak[0]} days")

# social()

# import matplotlib.pyplot as plt

# def accuracy_visual(correct, questions):
    
#     correct_perc = round((int(correct) / int(questions)) * 100)
#     data = [100-correct_perc, correct_perc] # Add up to 100
#     labels = ['Incorrect', 'Correct']
#     colors = ['tab:red', 'tab:green']
#     explode = (0.1, 0)  # Explode the 1st slice (Dogs)

#     plt.pie(data, labels=labels, colors=colors, explode=explode, shadow=True, autopct='%1.1f%%')
#     plt.title('Accuracy')
#     plt.show()

# accuracy_visual(3,5)

# fake = Faker()
# print(fake.first_name())

# print(dt.datetime.now())

# def y(x):
#     return x+x
# def funcmanipulate(func=lambda x: x+x, v=0):
#     func(v)
# funcmanipulate(5)

# print(y(2))

# species = ('Adelie', 'Chinstrap', 'Gentoo')
# sex_counts = {
#     'Male': np.array([73, 34, 61]),
#     'Female': np.array([73, 34, 58]),
# }
# width = 0.6  # the width of the bars: can also be len(x) sequence


# fig, ax = plt.subplots()
# bottom = np.zeros(3)

# for sex, sex_count in sex_counts.items():
#     p = ax.bar(species, sex_count, width, label=sex, bottom=bottom)
#     bottom += sex_count

#     ax.bar_label(p, label_type='center')

# ax.set_title('Number of penguins by sex')
# ax.legend()

# plt.show()





# import csv
# def read_file(): # Turns a file into a list of dictionary characters
#     characs = []
#     with open("battle_simulator/characters.csv", "r") as file:
#         reader = csv.reader(file)
#         for row_index, row in enumerate(reader):
#             if row_index == 0:
#                 detail_types = row
#                 continue
#             dict = {}
#             for detail_index, detail in enumerate(row):
#                 if detail_index == 2 or detail_index == 3 or detail_index == 4 or detail_index == 5 or detail_index == 6 or detail_index == 7:
#                     detail = int(detail)
#                 dict.update({detail_types[detail_index]:detail})
#             characs.append(dict)
#     return characs

# def find(prompt, characs):
#     ind = -1
#     charac_name = input(prompt).strip()
#     for charac_ind, charac in enumerate(characs):
#         if charac_name.upper() == charac["Name"].upper():
#             ind = charac_ind
#     return charac_name, ind

# characs = read_file()
# charac_name, ind = find("Which character do you want to see a stat visual of?:\n", characs)
# if ind == -1:
#     print(f"\n{charac_name} Can't Be Found")

# species = ('Health', 'Strength', 'Defense', 'Speed')
# sex_counts = {
#     'Stat': np.array([characs[ind]["Health"], characs[ind]["Strength"], characs[ind]["Defense"], characs[ind]["Speed"]])
# }
# width = 0.4  # the width of the bars: can also be len(x) sequence
# fig, ax = plt.subplots()
# bottom = np.zeros(4)
# for sex, sex_count in sex_counts.items():
#     p = ax.bar(species, sex_count, width, label=sex, bottom=bottom)
#     bottom += sex_count
#     ax.bar_label(p, label_type='center')
# ax.set_title("Character's Stats")
# ax.legend()
# plt.show()




# import pandas as pd

# data = {'col1': [1, 2, 3, 4, 5], 'col2': [6, 7, 8, 9, 10]}
# df = pd.DataFrame(data)

# mean_col1 = df['col1'].mean()
# mean_col2 = df['col2'].mean()
# print(f'{mean_col1=}') # Output: mean_col1=3.0
# print(f'{mean_col2=}') # Output: mean_col2=8.0

# # Mean of all columns
# mean_all = df.mean()
# print(f'{mean_all=}')
# # Output:
# # mean_all=col1    3.0
# # col2    8.0
# # dtype: float64


# median_col1 = df['col1'].median()
# median_col2 = df['col2'].median()
# print(f'{median_col1=}') # Output: median_col1=3.0
# print(f'{median_col2=}') # Output: median_col2=8.0


# data_with_mode = {'col1': [1, 2, 2, 3, 4, 4, 4, 5]}
# df_mode = pd.DataFrame(data_with_mode)
# mode_col1 = df_mode['col1'].mode()
# print(f'{mode_col1=}')
# Output:
# mode_col1=0    4
# dtype: int64