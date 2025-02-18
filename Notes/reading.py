# Luke Murdock, Reading Notes Python
import csv

'''
How do you open a file in your program?
How do you alter text to work as data in a program?
What is a CSV file Download CSV file?
How are they used in programming?
'''

with open("Notes/test.txt", "r") as file:
    content = file.read()
    print(content[5:20].upper())

print(content)

file = open("Notes/test.txt", "r").read()

users = {}

with open("Notes/Class CSV sample - Sheet1.csv") as file:
    reader = csv.reader(file)
    print(reader)
    next(reader)
    for row in reader:
        print(row)
        users.update({row[0]:row[1]})
print(users)

