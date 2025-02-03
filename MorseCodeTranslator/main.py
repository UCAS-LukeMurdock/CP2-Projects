# Luke Murdock, Simple Morse Code Translator

eng_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

morse_letters = ['._', '_...', '_._.', '_..', '.', '.._.', '__.', '....', '..', '.___', '_._', '._..', '__', '_.', '___', '.__.', '__._', '._.', '...', '_', '.._', '..._', '.__', '_.._', '_.__', '__..']

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

def morse(): # Translates a word into Morse
    while True:
        word = input("Type the English word you want translated into Morse:\n").lower()
        code = ""
        list(word)

        for letter in word:
            correct = False
            for eng_ind, eng_letter in enumerate(eng_letters):
                if letter == eng_letter:
                    code += f"{morse_letters[eng_ind]} "
                    correct = True
                    break
            if correct == False:
                print("Contains Special Characters. Try Again")
                break
        if correct == False:
            continue
        elif correct == True:
            print(f"In Morse Code: {code}")
        break

def english(): # Translates Morse Code into an English word
    while True:
        code = input("Type the Morse you want translated into English:\n")
        word = ""
        code = code.split(" ")

        for letter in code:
            correct = False
            for morse_ind, morse_letter in enumerate(morse_letters):
                if letter == morse_letter:
                    word += f"{eng_letters[morse_ind]}"
                    correct = True
                    break
            if correct == False:
                print("Contains Incorrect Morse Code. Try Again")
                break
        if correct == False:
            continue
        elif correct == True:
            print(f"In English: {word.upper()}")
        break

def main(): # Lets user choose what they want their text translated into
    print("Welcome, this program lets you change English into Morse Code and vice versa.")
    while True:
        choice = num_input("\nInto Morse Code(1) Into English(2) Exit(3)\n", "int", 3)
        if choice == 1:
            morse()
        elif choice == 2:
            english()
        elif choice == 3:
            break
        else:
            print("Something Broke")

main()