# To-Do List Application

## Description
A simple To-Do List application with functionalities to add tasks, view tasks, mark tasks as complete, delete tasks, and save/load tasks using a JSON file for persistent storage.

## Requirements
- Python 3.x
- `customtkinter` library
- `Pillow` library for image handling


## File Structure
- `images` : Contains the images for buttons
- `task.py`: Contains the `Task` class that defines a task object.
- `storage.py`: Handles saving, loading, and updating task completion status.
- `gui.py`: Contains the graphical user interface using `customtkinter`.
- `tasks.json`: JSON file used to store tasks (auto-generated).

## How to Run
1. Run the GUI by executing : `python gui.py`
2. The application window will open, allowing you to add tasks, view tasks, mark the last task as complete, delete the last task, and exit the app.

## Features
- **Add Task**: Enter the title, description, category, and optional deadline to add a task.
- **View Tasks**: Shows all tasks in a list format.
- **Mark Last Task as Complete**: Marks the most recently added task as complete.
- **Delete Last Task**: Removes the most recently added task.
- **Exit**: Saves all tasks to `tasks.json` before exiting.

## Notes
- Ensure that the `images` folder contains the icons (`add_icon.png`, `view_icon.png`, etc.).
- JSON file (`tasks.json`) will be created/updated automatically when tasks are added, marked complete, or deleted.

## Troubleshooting
- If an error occurs regarding deadlines, ensure that the date format is `YYYY-MM-DD`.


