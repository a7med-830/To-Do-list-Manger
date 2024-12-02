import os
import pyfiglet
import time

def menu():
    global isrunning
    clear_screen()
    print(pyfiglet.figlet_format("To DO List Manger"))  
    for char in "Main Menu\n":
        print(char, end="", flush=True)  
        time.sleep(0.1)
    print("[1] Add Task \n[2] View Tasks \n[3] Delete Tasks \n[4] Delete current file")
    print("[q] Quit")

    choice = input("choose an option : ").lower()

    
    match choice:
        case '1':
            clear_screen()
            addTask()
        case '2':
            clear_screen()
            TaskView()
        case '3':
            clear_screen()
            deleteTask()
        case '4':
            clear_screen()
            deleteFile()
        case 'q':
            isrunning = False
        case _:
            print ("invalid choice!")
            clear_screen()
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

        print("Task add successfully! ✅")

        if input("do you want to add any other tasks? [y/n] : ").lower() == "n":
            clear_screen()
            break

def deleteTask():
    if os.path.exists("Tasks.txt"):

        with open("Tasks.txt", "r") as tasksFile:
            lines = tasksFile.readlines()  

        print("-" * 50)
        print("Your Tasks📋 : ")
        for i, line in enumerate(lines, start=1):
            print(f"[{i}] {line.strip()}")  
        print("-" * 50)

        choice = input("[a] Delete all tasks \nEnter the task number to delete: ").lower()

        if choice == 'a':  
            open("Tasks.txt", "w").close()  
            print("All tasks have been deleted! ✅")
            
        elif choice.isdigit():  
            task_number = int(choice) - 1  

            if 0 <= task_number < len(lines):
                del lines[task_number]  
                with open("Tasks.txt", "w") as tasksFile:
                    tasksFile.writelines(lines)  
                print(f"Task {choice} has been deleted! ✅")
                input("press 'Enter' to go back to Main Menu")
            else:
                print("Invalid task number! ❌")
                deleteTask()

        else:
            print("Invalid input! ❌")
            deleteTask()
    else:
        print("File not found! ❌")
        input("press 'Enter' to go back to Main Menu")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def TaskView():
    try:
        tasksFile = open("Tasks.txt", "r")
    except FileNotFoundError:
        print("File not found! ❌")
        input("press 'Enter' to go back to Main Menu")
    print ("-" * 50)
    print("Your Tasks📋 : ")
    for line in tasksFile.readlines():
        print(line.strip())
    print ("-" * 50)
    tasksFile.close
    input("press 'Enter' to go back to Main Menu")

def deleteFile():
    if os.path.exists("Tasks.txt"):
        try:
            os.remove("Tasks.txt")
            print("file deleted successfully! ✅")
        except PermissionError:
            print("Something is wrong❌")

    else:
        print("The file is deleted already! ❌")
    input("press 'Enter' to go back to Main Menu")
    clear_screen()

if not os.path.exists("Tasks.txt"):
    tasksFile = open("Tasks.txt", "x")
    tasksFile.close

isrunning = True
while isrunning:
    menu()

if isrunning == False:
    clear_screen()
    print(pyfiglet.figlet_format("To DO List Manger"))
    print("Made By Ahmed EL-Shekih")
    print("GitHub : @a7med-830")
    print("Exiting in 5 seconds", end="")
    for point in ".....":
        print(point, end="", flush=True)
        time.sleep(1)
