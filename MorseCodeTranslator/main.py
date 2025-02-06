# Luke Murdock, Simple Morse Code Translator

eng_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']
morse_letters = ['._', '_...', '_._.', '_..', '.', '.._.', '__.', '....', '..', '.___', '_._', '._..', '__', '_.', '___', '.__.', '__._', '._.', '...', '_', '.._', '..._', '.__', '_.._', '_.__', '__..', ' / ']

def num_input(prompt, data_type, range = 0): # Checks and solves errors in int and float inputs
    while True:
        try: 
            if data_type == "int":
                response = int(input(prompt))
            elif data_type == "float":
                response = float(input(prompt))
        except ValueError:
            print("Invalid Input Type")
            continue
        if range == 0 or (response > 0 and response <= range):
            break
        else:
            print("Not In Range")
            continue 
    return response

def text(to_morse): # Asks for text then prepares it (Turns it into list to be manipulated later) for either the morse or english translation
    while True:
        # When 'which' is True it prepares translation to Morse, when False it prepares translation to English
        text = input(f"Type the {'English' if to_morse == True else 'Morse'} you want translated into {'Morse' if to_morse == True else 'English (Put / for space)'}:\n").lower()
        text = text.split(f"{' ' if to_morse == True else ' / '}")
        for item_ind, item in enumerate(text):
            if to_morse == True:
                text[item_ind] = list(item)
            elif to_morse == False:
                print(text[item_ind])
                text[item_ind] = item.split(' ')
                print(text[item_ind])
                text[item_ind].append(' / ')
                print(text)
                
        if to_morse == True:
            if morse(text) == True:
                break
            else:
                continue
        elif to_morse == False:
            if english(text) == True:
                break
            else:
                continue

def morse(words): # Translates words into Morse (Compares lists), if it doesn't have special characters, then formats and prints it
    correct = False
    code = ""
    for word in words:
        for letter in word:
            correct = False
            for eng_ind, eng_letter in enumerate(eng_letters):
                if letter == eng_letter:
                    code += f"{morse_letters[eng_ind]} "
                    correct = True
                    break
            if correct == False:
                break
        if correct == False:
            print("Contains Special Characters. Try Again")
            break
        code = code.rstrip()
        code += " / "
    if correct == False:
        return False
    elif correct == True:
        code = code[:-3]
        print(f"In Morse Code: {code}")
    return True

def english(codes): # Translates Morse Code into English, if it has correct characters, then formats and prints it
    correct = False
    word = ""
    for code in codes:
        for letter in code:
            correct = False
            for morse_ind, morse_letter in enumerate(morse_letters):
                if letter == morse_letter:
                    word += f"{eng_letters[morse_ind]}"
                    correct = True
                    break
            if correct == False:
                break
        if correct == False:
            print("Contains Incorrect Morse Code. Try Again")
            break
        code += " "
    if correct == False:
        return False
    elif correct == True:
        print(f"In English: {word.upper()}")
    return True

def main(): # Welcomes user, then lets them choose to either translate into English or Morse
    print("Welcome, this program lets you change English into Morse Code and vice versa.")
    while True:
        choice = num_input("\nInto Morse Code(1) Into English(2) Exit(3)\n", "int", 3)
        if choice == 1:
            text(True)
        elif choice == 2:
            text(False)
        elif choice == 3:
            break
        else:
            print("Something Broke")

main()
