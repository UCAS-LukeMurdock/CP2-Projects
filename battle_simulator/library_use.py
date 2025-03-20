# Luke Murdock, This file uses the libraries for the updated battle simulator, such as Stat Visuals, Data Analysis and Fake Character Maker

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from faker import Faker
from file_handler import read_file, intput, find

def visual(): # Shows a visual bar graph of a desired character's stats in a new window
    characs = read_file()
    charac_name, ind = find("Which character do you want to see a stat visual of?:\n", characs)
    if ind == -1:
        print(f"\n{charac_name} Can't Be Found")
        return
    stats = ('Health', 'Strength', 'Defense', 'Speed')
    stat_counts = [characs[ind]["Health"], characs[ind]["Strength"], characs[ind]["Defense"], characs[ind]["Speed"]]
    width = 0.6
    fig, ax = plt.subplots()
    bottom = np.zeros(4)
    for stat, stat_count in stat_counts:
        p = ax.bar(stats, stat_count, width, label=stat, bottom=bottom)
        bottom += stat_count
        ax.bar_label(p, label_type='center')
    ax.set_title("Character's Stats")
    ax.legend()
    plt.show()

def analysis(): # Displays a data analysis, including the mean, median, and mode, for a desired character's stats
    characs = read_file()
    charac_name, ind = find("Which character do you want to see a data analysis of?:\n", characs)
    if ind == -1:
        print(f"\n{charac_name} Can't Be Found")
        return
    data = {'col1': [characs[ind]["Health"], characs[ind]["Strength"], characs[ind]["Defense"], characs[ind]["Speed"]]}
    df = pd.DataFrame(data)
    mean = df['col1'].mean()
    print(f'\nMean of Stats: {mean}')
    median = df['col1'].median()
    print(f'Median of Stats: {median}')
    mode = df['col1'].mode()
    print(f'Mode of Stats: {'None' if '1   ' in str(mode) else str(mode)[5:7]}')

def characs_visual_analysis(): # Shows a bargraph of all of the characters' average stat amounts in a new window
    pass

def fake_character(): # Displays a fake character with a name, backstory, hometown, and birthdate
    fake = Faker()
    print(f"\nName: {fake.name()}\nBackstory: {fake.text()}\nHometown: {fake.local_latlng()[4].split("/")[1]}\nBirthdate: {fake.date_of_birth()}")
    retry = intput(f"\nRegenerate(1) Continue(2)\n", 1,2)
    if retry == 1:
        fake_character()
        return