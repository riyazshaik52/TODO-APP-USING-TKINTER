class Task:
    def __init__(self, title, description, category, deadline=None, completed=False):
        self.title = title
        self.description = description
        self.category = category
        self.deadline = deadline  # Added deadline attribute
        self.completed = completed

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "Completed" if self.completed else "Not Completed"
        deadline_str = f" | Deadline: {self.deadline.strftime('%Y-%m-%d')}" if self.deadline else ""
        return f"[{status}] {self.title} - {self.category}{deadline_str}: {self.description}"
