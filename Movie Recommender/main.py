#Luke Murdock, Movie Recommender
import csv

movies = []

def num_input(prompt, range = 0, data_type = "int"): # Checks and solves errors in int and float inputs (Has Range If Needed)
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

# 
with open("Movie Recommender\Movies list.csv", "r") as file:
    reader = csv.reader(file)
    print(reader)
    for row_index, row in enumerate(reader):
        if row_index == 0:
            detail_types = row
            continue
        print(row)
        movie = {}
        for detail_index, detail in enumerate(row):
            movie.update({detail_types[row_index]:row[row_index]})
        movies.append({detail_types[row_index]:row[row_index]})
print(movies)

def display(): # 
    print("")

def recommend(): # 
    print("\nFilter Options: Genre(1) Directors(2) Length(3) Actors(3)")
    filter_1 = input("\nFirst Filter: ")
    filter_2 = input("Second Filter: ")

def main(): # 
    pass