#Luke Murdock, To Do List
import csv

'''
Create a to do list (Kept on a txt file)
Add items to the to do list
Mark item as complete
Delete item from to do list
'''
tasks = []
# 
with open("To Do List/list.csv", "r") as file:
    reader = csv.reader(file)
    for row_index, row in enumerate(reader):
        if row_index == 0:
            detail_types = row
            continue
        task = {}
        for detail_index, detail in enumerate(row):
            task.update({detail_types[detail_index]:row[detail_index]})
        tasks.append(task)

def num_input(prompt, range = 0, data_type = "int"): # Checks and solves errors in int and float inputs (Has Range If Needed)
    while True:
        try: 
            if data_type == "int":
                response = int(input(prompt).strip())
            elif data_type == "float":
                response = float(input(prompt).strip())
        except ValueError:
            print("Invalid Input Type")
            continue
        if range == 0 or (response > 0 and response <= range):
            break
        else:
            print("Not In Range")
            continue
    return response

def display(): # Prints all of the to-do list's tasks
    print("\nTo-Do List:\n")
    if tasks == []:
        print("None")
    for task in tasks:
        print(f"Task- {task["Name"]}\nStatus- {task["Status"]}\n")

def add(): # 
    name = input("Task: ").strip()
    tasks.append({"Name": name, "Status": "Not Done"})
    write()
    


def mark(): # 
    choice = num_input("\nMark(1) Unmark(2) Exit(3)\n", 3)
    status = "Done"
    if choice == 2:
        status = f"Not {status}"
    elif choice == 3:
        return
    name = input("Desired Task: ").strip()
    for task in tasks:
        if name.lower() == task["Name"].lower():
            task["Status"] = status
    write()

def delete(): # 
    print("")

def write(): # 
    with open ("To Do List/list.csv", "w", newline="") as file:
        fieldnames = ["Name", "Status"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(tasks)

def main(): # Introduces the program and then lets the user choose one of the options
    print("Welcome to this to-do list program that lets you add, mark complete, unmark, or delete a task from the list")
    while True:
        choice = num_input("\nDisplay(1) Add(2) Mark or Unmark(3) Delete(4) Exit(5)\n", 5)
        if choice == 1:
            display()
        elif choice == 2:
            add()
        elif choice == 3:
            mark()
        elif choice == 4:
        elif choice == 5:
            delete()
        elif choice == 6:
            print("Come Back Soon!")
            break
        else:
            print("Something Broke")
            continue

main()