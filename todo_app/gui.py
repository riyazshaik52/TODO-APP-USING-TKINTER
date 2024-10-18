import customtkinter as ctk
from tkinter import messagebox
from storage import load_tasks, save_tasks, mark_task_completed  # Import the new function
from task import Task
from PIL import Image
from datetime import datetime

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")
        
        # Center the window on startup
        self.center_window(700, 600)
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")
        self.tasks = load_tasks()

        self.title_var = ctk.StringVar()
        self.desc_var = ctk.StringVar()
        self.cat_var = ctk.StringVar()
        self.deadline_var = ctk.StringVar()
        self.complete_title_var = ctk.StringVar()  # New variable for completing a task

        # Load images
        self.add_icon = ctk.CTkImage(Image.open("images/add_icon.png"), size=(20, 20))
        self.view_icon = ctk.CTkImage(Image.open("images/view_icon.png"), size=(20, 20))
        self.delete_icon = ctk.CTkImage(Image.open("images/delete_icon.png"), size=(20, 20))
        self.exit_icon = ctk.CTkImage(Image.open("images/exit_icon.png"), size=(20, 20))

        self.setup_ui()

    def center_window(self, width, height):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        self.root.geometry(f"{width}x{height}+{x}+{y}")

    def setup_ui(self):
        self.root.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6), weight=1)
        self.root.grid_columnconfigure((0, 1), weight=1)

        self.bg_frame = ctk.CTkFrame(self.root, fg_color=("white", "#f0f0f0"), corner_radius=15)
        self.bg_frame.grid(row=0, column=0, rowspan=8, columnspan=2, padx=20, pady=20, sticky="nsew")

        title_frame = ctk.CTkFrame(self.bg_frame, fg_color="blue", corner_radius=10)
        title_frame.grid(row=0, column=0, columnspan=2, padx=20, pady=(20, 10), sticky="ew")
        title_label = ctk.CTkLabel(title_frame, text="To-Do List", font=("Arial", 24, "bold"), text_color="white")
        title_label.pack(padx=10, pady=5)

        task_title_label = ctk.CTkLabel(self.bg_frame, text="Task Title", font=("Arial", 16, "bold"), text_color="#333")
        task_title_label.grid(row=1, column=0, padx=(30, 10), pady=(10, 10), sticky="w")
        title_entry = ctk.CTkEntry(self.bg_frame, textvariable=self.title_var, width=400, font=("Arial", 14), corner_radius=10)
        title_entry.grid(row=1, column=1, padx=(10, 30), pady=(10, 10))

        desc_label = ctk.CTkLabel(self.bg_frame, text="Description", font=("Arial", 16, "bold"), text_color="#333")
        desc_label.grid(row=2, column=0, padx=(30, 10), pady=10, sticky="w")
        desc_entry = ctk.CTkEntry(self.bg_frame, textvariable=self.desc_var, width=400, font=("Arial", 14), corner_radius=10)
        desc_entry.grid(row=2, column=1, padx=(10, 30), pady=10)

        cat_label = ctk.CTkLabel(self.bg_frame, text="Category", font=("Arial", 16, "bold"), text_color="#333")
        cat_label.grid(row=3, column=0, padx=(30, 10), pady=10, sticky="w")
        cat_entry = ctk.CTkEntry(self.bg_frame, textvariable=self.cat_var, width=400, font=("Arial", 14), corner_radius=10)
        cat_entry.grid(row=3, column=1, padx=(10, 30), pady=10)

        deadline_label = ctk.CTkLabel(self.bg_frame, text="Deadline (YYYY-MM-DD)", font=("Arial", 16, "bold"), text_color="#333")
        deadline_label.grid(row=4, column=0, padx=(30, 10), pady=10, sticky="w")
        deadline_entry = ctk.CTkEntry(self.bg_frame, textvariable=self.deadline_var, width=400, font=("Arial", 14), corner_radius=10)
        deadline_entry.grid(row=4, column=1, padx=(10, 30), pady=10)

        # New section for marking a task as complete
        complete_label = ctk.CTkLabel(self.bg_frame, text="Complete Task (Enter Title)", font=("Arial", 16, "bold"), text_color="#333")
        complete_label.grid(row=5, column=0, padx=(30, 10), pady=(10, 10), sticky="w")
        complete_entry = ctk.CTkEntry(self.bg_frame, textvariable=self.complete_title_var, width=400, font=("Arial", 14), corner_radius=10)
        complete_entry.grid(row=5, column=1, padx=(10, 30), pady=(10, 10))

        button_width = 200
        add_button = ctk.CTkButton(self.bg_frame, text="Add Task", command=self.add_task, width=button_width,
                                   font=("Arial", 14, "bold"), fg_color="#4CAF50", hover_color="#45A049",
                                   corner_radius=8, image=self.add_icon, compound="left")
        add_button.grid(row=6, column=0, padx=(30, 10), pady=20, sticky="e")

        complete_button = ctk.CTkButton(self.bg_frame, text="Mark as Complete", command=self.mark_task_as_complete, width=button_width,
                                         font=("Arial", 14, "bold"), fg_color="#2196F3", hover_color="#1E88E5",
                                         corner_radius=8)
        complete_button.grid(row=6, column=1, padx=(10, 30), pady=20, sticky="w")

        view_button = ctk.CTkButton(self.bg_frame, text="View Tasks", command=self.view_tasks, width=button_width,
                                    font=("Arial", 14, "bold"), fg_color="#2196F3", hover_color="#1E88E5",
                                    corner_radius=8, image=self.view_icon, compound="left")
        view_button.grid(row=7, column=0, padx=(30, 10), pady=20, sticky="w")

        delete_button = ctk.CTkButton(self.bg_frame, text="Delete Last Task", command=self.delete_last_task, width=button_width,
                                       font=("Arial", 14, "bold"), fg_color="#FF5722", hover_color="#E64A19",
                                       corner_radius=8, image=self.delete_icon, compound="left")
        delete_button.grid(row=7, column=1, padx=(10, 30), pady=20, sticky="w")

        exit_button = ctk.CTkButton(self.bg_frame, text="Exit", command=self.exit_app, width=button_width,
                                    font=("Arial", 14, "bold"), fg_color="#F44336", hover_color="#E53935",
                                    corner_radius=8, image=self.exit_icon, compound="left")
        exit_button.grid(row=8, column=0, columnspan=2, pady=(10, 30))

    def add_task(self):
        title = self.title_var.get()
        description = self.desc_var.get()
        category = self.cat_var.get()
        deadline = self.deadline_var.get()

        # Validate deadline input
        if title and description and category:
            try:
                deadline_date = datetime.strptime(deadline, "%Y-%m-%d") if deadline else None
                task = Task(title, description, category, deadline_date)
                self.tasks.append(task)
                messagebox.showinfo("Success", "Task added successfully!")
                self.title_var.set("")
                self.desc_var.set("")
                self.cat_var.set("")
                self.deadline_var.set("")
            except ValueError:
                messagebox.showerror("Error", "Invalid deadline format! Please use YYYY-MM-DD.")
        else:
            messagebox.showerror("Error", "All fields are required!")

    def mark_task_as_complete(self):
        title = self.complete_title_var.get()
        if title:
            if mark_task_completed(self.tasks, title):
                messagebox.showinfo("Success", f"Task '{title}' marked as complete!")
                self.complete_title_var.set("")  # Clear the entry after completion
            else:
                messagebox.showerror("Error", f"Task '{title}' not found.")
        else:
            messagebox.showerror("Error", "Please enter the task title.")

    def view_tasks(self):
        if not self.tasks:
            messagebox.showinfo("Info", "No tasks available.")
            return
        
        tasks_str = "\n".join([f"{i+1}. {task}" for i, task in enumerate(self.tasks)])
        messagebox.showinfo("Tasks", tasks_str)

    def delete_last_task(self):
        if self.tasks:
            removed_task = self.tasks.pop()
            messagebox.showinfo("Task Deleted", f"Deleted task: {removed_task.title}")
        else:
            messagebox.showinfo("Info", "No tasks available to delete.")

    def exit_app(self):
        save_tasks(self.tasks)
        self.root.quit()

if __name__ == "__main__":
    root = ctk.CTk()
    app = ToDoApp(root)
    root.mainloop()
