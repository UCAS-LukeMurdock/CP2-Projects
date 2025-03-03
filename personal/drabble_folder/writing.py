# Luke Murdock, Writing
import datetime as dt, random as r
from file_handler import read_file as read, write_file as write

def free_write(signed_in, prompts, vocab_words, want_prompt, person_ind, want_fire): # 
    writing = input(f"{prompts[r.randrange(0,len(prompts))] if want_prompt == True else 'Free-Write'}:\n")
    words = writing.strip().split(" ")
    for word in words:
        if word == "":
            words.remove(word)
    word_count = len(words)
    print(f"    Word Count: {word_count}\n")
    print("You Did The Free-Write!")
    if signed_in == True:
        streak_add(person_ind, want_fire)
    return word_count

def streak_add(person_ind, want_fire):
    users = read()
    day = str(dt.datetime.now())[:10]
    if day != users[person_ind]["Day"]:
        users[person_ind]["Streak"] = int(users[person_ind]["Streak"]) +1
        users[person_ind]["Day"] = day
        print(f"Your Streak has Increased to {users[person_ind]["Streak"]}{f'🔥' if want_fire == True else ''}!")
        write(users)

def streak_check(person_ind):
    users = read()
    day = str(dt.datetime.now())[:10]
    time_since = day[-2:] - users[person_ind]["Day"][-2:] # Ex: 2025-03-02
    if time_since <= 1:
        return
    elif time_since > 1:
        users[person_ind]["Streak"] = 0
        print("You Lost Your Streak!")
        write(users)

def display_prompt(prompts):
    print(f"Prompt for Writing Ideas:\n{prompts[r.randrange(0,len(prompts))]}")

def word(vocab_words):
    print(f"Vocabulary Word:\n{vocab_words[r.randrange(0,len(vocab_words))]}")