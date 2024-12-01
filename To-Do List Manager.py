# Allow users to add, delete, and view tasks.
# Save tasks to a file for persistence.
def menu():
    print("Main menu")
    print("[1] Add Task \n [2] View Tasks ")
    print("[q] Quit")

    choice = input("choose an option").lower()

    match choice:
        case '1':
            addTask()
        case '2':
            TaskView()
        case 'q':
            isrunning = False
            return isrunning


def addTask():
    while True:
        toDo = input("Enter your task : ")
        toDoNum = input("Enter your task number : ")
        toDoList.update({ toDoNum : toDo })
        print(toDoList)
        if input("do you want to add any other tasks? [y/n] : ").lower() == "n":
            break

def TaskView():
    for taskNum,task in toDoList:
        print(f"{taskNum} : {task}")


toDoList = {}
isrunning = True
addTask()

if input("do you want to add any other tasks? [y/n] : ").lower() == "y":
    addTask()





