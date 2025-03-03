# Luke Murdock, File Handling and Input Handling
import csv

def int_input(prompt, range = 0, zero = False): # Checks and solves errors in integer inputs (Has Range If Needed)
    while True:
        try: 
            response = int(input(prompt).strip())
        except ValueError:
            print("Invalid Input Type")
            continue
        if range == 0 or (response > 0 and response <= range and zero == False) or (zero == True and range >= 0 and response <= range):
            break
        else:
            print("Not In Range")
            continue
    return response

def read_file():
    users = []
    with open("personal/drabble_folder/main_users.csv", "r") as file:
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
            users.append(dict)
    return users

def write_file(users): # Writes the list of dictonary profiles onto the file
    with open ("personal/drabble_folder/main_users.csv", "w", newline="") as file:
        fieldnames = ["Name","Streak","Day","Coins","Gems","Bought","Storage"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(users)