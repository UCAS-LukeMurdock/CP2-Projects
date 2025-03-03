# Luke Murdock, Drabble Settings
from file_handler import int_input

def settings(want_fire, want_prompt, want_money):
    while True:
        change = int_input(f"""
Settings
    What do you want changed? [Exit(0)]:
    Fire Emojis- {f'Activated [🔥] ' if want_fire == True else 'Deactivated'}(1)
    Write With Prompt- {'Activated [❔] ' if want_prompt == True else 'Deactivated'}(2)
    Shop- {'Activated [💸] ' if want_money == True else 'Deactivated'}(3)
""", 3, zero = True)
        if change == 0:
            return want_fire, want_prompt, want_money
        elif change == 1:
            want_fire = not want_fire
        elif change == 2:
            want_prompt = not want_prompt
        elif change == 3:
            want_money = not want_money