# Luke Murdock, Read Files, Integer Input Handler, and other Handlers
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
                if detail_index == 1:
                    detail = eval(detail)
                dict.update({detail_types[detail_index]:detail})
            characs.append(dict)
    return characs

def intput(prompt, min = -1, max = -1): # Checks and prompts user to solve errors in integer inputs (Has Range If Needed)
    try:
        response = int(input(prompt).strip())
    except:
        print("Not An Integer")
        response = intput(prompt,min,max)
    if (min != -1 or max != -1) and (response < min or response > max): # If either min or max aren't -1 and the input is out of range then the user has to reinput
        print(f"Not In Range: {min}-{max}")
        response = intput(prompt,min,max)
    return response