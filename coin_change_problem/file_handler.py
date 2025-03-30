# Luke Murdock, Read File
import csv

def read_file(): # Turns a file into a list of dictionaries
    dicts = []
    with open("coin_change_problem\coins.csv", "r") as file:
        reader = csv.reader(file)
        for row_index, row in enumerate(reader):
            if row_index == 0:
                detail_types = row
                continue
            dict = {}
            for detail_index, detail in enumerate(row):
                if detail_index == 2:
                    detail = eval(detail)
                dict.update({detail_types[detail_index]:detail})
            dicts.append(dict)
    return dicts