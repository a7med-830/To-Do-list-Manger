
# To-Do List Manager  

A simple Python-based command-line application to manage your daily tasks. You can add, view, delete individual tasks, or even clear all tasks. The tasks are saved to a file for persistence, ensuring your data is retained between program executions.

---

## Features
- Add tasks with an auto-assigned number.
- View all tasks in an organized, numbered list.
- Delete specific tasks by selecting their number.
- Clear all tasks or delete the tasks file entirely.
- Tasks are stored in a file (`Tasks.txt`) for persistence.

---

## Language Used
- **Language**: Python
- **Modules**: 
  - `os` for file and system operations.
  - `pyfiglet` for ASCII art.
  - `time` for visual enhancements.
---

## Usage
1. Launch the application
2. Follow the on-screen menu options:
   - `[1] Add Task`: Add a new task to the list.
   - `[2] View Tasks`: Display all saved tasks.
   - `[3] Delete Tasks`: Remove a specific task or all tasks.
   - `[4] Delete File`: Delete the entire task file (`Tasks.txt`).
   - `[q] Quit`: Exit the program.

---

## How It Works
### File Management
- Tasks are saved in a plain text file named `Tasks.txt`.
- If the file doesn’t exist, it’s automatically created.

### Task Numbering
- Task numbers are automatically assigned and re-numbered after any deletion.

### Persistence
- Tasks remain in the file even after the program is closed, ensuring you don’t lose your data.

---

## Author
- **Ahmed**  
  - GitHub: [a7med-830](https://github.com/a7med-830)  

Feel free to reach out for any suggestions or improvements! 😊  
