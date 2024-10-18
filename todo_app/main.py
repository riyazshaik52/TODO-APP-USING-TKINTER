from gui import ToDoApp
import customtkinter as ctk

if __name__ == "__main__":
    root = ctk.CTk()
    app = ToDoApp(root)  # This initializes the ToDoApp, which contains all functionality.
    root.mainloop()  # Starts the application.
