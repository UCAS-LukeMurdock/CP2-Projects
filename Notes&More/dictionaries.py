# Luke Murdock, Notes for Dictionaries

car = {
    "make": "Ford",
    "model": "Escape xlt",
    "year": 2008,
    "color": "Red",
    "name": "Freya"
}
#print(car["model"])

students = {
    "first": {
        1: "Vincent",
        2: "Cecily",
        3: "Evan"
    },
    "sixth": {
        1: "Nicole",
        2: "Luke",
        3: "Gavin",
        4: "Jackson"
    }
}

#print(students["sixth"][2])

print(students)
print(list(students.keys())[1])

print(students)