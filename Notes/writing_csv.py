# Luke Murdock, CSV file writing

import csv

data = [
    {"name": "john", "color": "jnr"},
    {"name": "jhn", "color": "jot"},
    {"name": "jn", "color": "jny"},
    {"name": "jon", "color": "hni"},
    {"name": "joh", "color": "jonh"},
    {"name": "ohn", "color": "jond"},
]
data.pop()
with open ("Notes/Class CSV sample - Sheet1.csv", "a", newline="") as file:
    fieldnames = ["name", "color"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)

with open ("Notes/Class CSV sample - Sheet1.csv", "r", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            print(f"user name: {row[0]}\ncolor: {row[1]}\n")

# [["silly_name", "Black"], ["silly", "lack"], ["name", "Blak"], ["sill", "rock"]]