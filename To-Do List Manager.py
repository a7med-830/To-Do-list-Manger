# Allow users to add, delete, and view tasks.
# Save tasks to a file for persistence.

import os

def menu():
    global isrunning
    print("Main menu")
    print("[1] Add Task \n[2] View Tasks \n[3] Delete Tasks \n[4] Delete current file")
    print("[q] Quit")

    choice = input("choose an option : ").lower()

    
    match choice:
        case '1':
            addTask()
        case '2':
            TaskView()
        case '3':
            deleteTask()
        case '4':
            deleteFile()
        case 'q':
            isrunning = False
        case _:
            print ("invalid choice!")
            menu()
    

    return isrunning


def addTask():
    while True:
        toDo = input("Enter your task : ")
        with open("Tasks.txt", "r") as tasksFile:
            tasks = tasksFile.readlines()

        with open("Tasks.txt", "a") as tasksFile:  
            toDoNum = len(tasks) + 1
            tasksFile.write(f"{toDoNum}- {toDo}\n")

        print("Task add successfully!")

        if input("do you want to add any other tasks? [y/n] : ").lower() == "n":
            break

def deleteTask():
    with open("Tasks.txt", "r") as tasksFile:
        lines = tasksFile.readlines()  

    print("-" * 50)
    print("Your Tasks:")
    for i, line in enumerate(lines, start=1):
        print(f"[{i}] {line.strip()}")  
    print("-" * 50)

    choice = input("[a] Delete all tasks \nEnter the task number to delete: ").lower()

    if choice == 'a':  
        open("Tasks.txt", "w").close()  
        print("All tasks have been deleted!")
        
    elif choice.isdigit():  
        task_number = int(choice) - 1  

        if 0 <= task_number < len(lines):
            del lines[task_number]  
            with open("Tasks.txt", "w") as tasksFile:
                tasksFile.writelines(lines)  
            print(f"Task {choice} has been deleted!")
        else:
            print("Invalid task number.")
            deleteTask()

    else:
        print("Invalid input!")
        deleteTask()



def TaskView():
    tasksFile = open("Tasks.txt", "r")
    print ("-" * 50)
    print("Your Tasks : ")
    for line in tasksFile.readlines():
        print(line.strip())
    print ("-" * 50)
    tasksFile.close

def deleteFile():
    if os.path.exists("Tasks.txt"):
        os.remove("Tasks.txt")
        print("file deleted successfully!")
    else:
        print("The file is deleted already!")

if not os.path.exists("Tasks.txt"):
    tasksFile = open("Tasks.txt", "x")
    tasksFile.close

isrunning = True

while isrunning:
    menu()

