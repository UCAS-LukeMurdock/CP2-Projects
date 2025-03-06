# Luke Murdock, File Handler and Int Input Handler
import csv

def read_file(): # Turns a file into a list of dictionary characters
    characs = []
    with open("battle_simulator/characters.csv", "r") as file:
        reader = csv.reader(file)
        for row_index, row in enumerate(reader):
            if row_index == 0:
                detail_types = row
                continue
            dict = {}
            for detail_index, detail in enumerate(row):
                if detail_index == 5:
                    detail = eval(detail)
                dict.update({detail_types[detail_index]:detail})
            characs.append(dict)
    return characs

def write_file(characs): # Writes the list of dictonary  onto the file
    with open ("battle_simulator/characters.csv", "w", newline="") as file:
        fieldnames = ["Name","Streak","Day","Coins","Gems","Bought","Storage"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(characs)

def intput(prompt, min = 0, max = 0): # Checks and prompts user to solve errors in integer inputs (Has Range If Needed)
    try:
        response = int(input(prompt).strip())
    except:
        print("Not An Integer")
        response = intput(prompt,min,max)
    if (min != 0 or max != 0) and (response < min or response > max): # If either min or max aren't 0 and the input is out of range then the user has to reinput
        print(f"Not In Range: {min}-{max}")
        response = intput(prompt,min,max)
    return response