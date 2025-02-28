#Luke Murdock, File Handler
from time_stamp import stamp

def count(file_path):
    words = []
    with open(file_path, "r") as file:
        content = file.read()
        lines = content.split("\n")
        for line in lines:
            words.extend(line.strip().split(" "))
    word_count = len(words)
    with open(file_path, "a") as file:
        file.write(f"\nWord Count: {word_count}    Time Stamp: {stamp()}")
    return "\nWord Count and Time Stamp Added!"