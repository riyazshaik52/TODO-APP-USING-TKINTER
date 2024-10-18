import json
from task import Task
from datetime import datetime

def save_tasks(tasks, filename='tasks.json'):
    with open(filename, 'w') as f:
        json.dump([task.__dict__ for task in tasks], f, indent=4)

def load_tasks(filename='tasks.json'):
    try:
        with open(filename, 'r') as f:
            tasks_data = json.load(f)
            # Convert deadline string back to datetime object if it exists
            for data in tasks_data:
                if data.get('deadline'):
                    data['deadline'] = datetime.strptime(data['deadline'], '%Y-%m-%d')
            return [Task(**data) for data in tasks_data]
    except FileNotFoundError:
        return []

def mark_task_completed(tasks, title):
    for task in tasks:
        if task.title == title:
            task.mark_completed()
            return True  # Return True if the task was found and marked
    return False  # Return False if the task was not found
