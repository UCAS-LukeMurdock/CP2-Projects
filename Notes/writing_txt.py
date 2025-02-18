#Luke Murdock, Writing to Text Files

'''
r = to read the file
w = write on the file (replaces the old file)
w+ read and write
a = append (adds to the file) (creates the file if it doesn't exist)
x = create a file
a+ = append and read the file
'''

with open("Notes/test.txt", "a") as file:
    file.write("\nHi!")
    