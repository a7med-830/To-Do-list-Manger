# Allow users to add, delete, and view tasks.
# Save tasks to a file for persistence.
def menu():
    global isrunning
    print("Main menu")
    print("[1] Add Task \n[2] View Tasks \n[3] Delete Tasks")
    print("[q] Quit")

    choice = input("choose an option : ").lower()

    # if choice == '1':
    #     addTask()
    # elif choice == '2':
    #     TaskView()
    # elif choice.lower() == 'q':
    #     isrunning = False


    match choice:
        case '1':
            addTask()
        case '2':
            TaskView()
        case '3':
            deleteTask()
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

def deleteTask():
    TaskView()
    toDoNum = input("[a] to delete all \nEnter the number of the task you want to delete : ")

    if toDoNum.lower() == 'a':
        toDoList.clear()
        print("Deleted all tasks successfully")
    else:
        del toDoList[toDoNum]
        print("Deleted selected Task successfully")
    



def TaskView():
    print ("-" * 50)
    print("Your Tasks : ")
    for taskNum,task in toDoList.items():
        print(f"{taskNum}- {task}")
    print ("-" * 50)




toDoList = {}
isrunning = True

while isrunning:
    menu()





