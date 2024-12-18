import tkinter as tk
from tkinter import messagebox, ttk
from tkcalendar import DateEntry
import json

# Initialize the main app window
root = tk.Tk()
root.title("Modern To-Do List App")
root.geometry("500x600")
root.config(bg="#1c1c1e")

# Global list to store tasks
tasks = []

# Load tasks from file on startup
def load_tasks():
    global tasks
    try:
        with open("tasks.json", "r") as f:
            tasks = json.load(f)
            update_listbox()
    except (FileNotFoundError, json.JSONDecodeError):
        tasks = []

# Save tasks to a JSON file automatically
def save_tasks():
    with open("tasks.json", "w") as f:
        json.dump(tasks, f)
        
# Function to update the listbox with tasks
def update_listbox(filter_text=""):
    listbox.delete(0, tk.END)
    for task in tasks:
        task_text = f"{task['task']} - Due: {task['due_date']} - Priority: {task['priority']}"
        if filter_text.lower() in task_text.lower():
            listbox.insert(tk.END, task_text)


# Function to add a task with due date and priority
def add_task():
    task_text = task_entry.get()
    due_date = due_date_entry.get_date().strftime("%Y-%m-%d")
    priority = priority_var.get()
    
    if not task_text:
        messagebox.showwarning("Warning", "Please enter a task.")
        return
    if priority == "Select Priority":
        messagebox.showwarning("Warning", "Please select a priority.")
        return
    
    tasks.append({"task": task_text, "due_date": due_date, "priority": priority})
    task_entry.delete(0, tk.END)
    priority_var.set("Select Priority")
    update_listbox()
    save_tasks()  # Automatically save after adding each task
    

# Function to delete a selected task
def delete_task():
    try:
        task_index = listbox.curselection()[0]
        del tasks[task_index]
        update_listbox()
        save_tasks()  # Automatically save after deleting a task
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")


# Function to clear all tasks
def clear_tasks():
    global tasks
    if messagebox.askyesno("Confirmation", "Do you really want to clear all tasks?"):
        tasks = []
        update_listbox()
        save_tasks()  # Automatically save after clearing all tasks

# Function to search tasks
def search_tasks():
    filter_text = search_entry.get()
    update_listbox(filter_text)


# GUI Elements

# Frame for listbox and scrollbar
frame = tk.Frame(root, bg="#1c1c1e")
frame.pack(pady=10)


# Listbox to display tasks with modern aesthetics
listbox = tk.Listbox(
    frame,
    width=50,
    height=12,
    font=("Helvetica", 12),
    selectmode=tk.SINGLE,
    bg="#2c2c2e",
    fg="#e4e4e6",
    selectbackground="#5e5ce6",
    highlightthickness=0,
    bd=0,
)
listbox.pack(side=tk.LEFT, fill=tk.BOTH, padx=10, pady=10)

# Scrollbar for the listbox
scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

# Entry box for adding new tasks
tk.Label(root, text="Task", font=("Helvetica", 12), bg="#1c1c1e", fg="#e4e4e6").pack(pady=(15, 5))
task_entry = tk.Entry(root, font=("Helvetica", 12), width=30, bg="#3a3a3c", fg="#e4e4e6", insertbackground="#e4e4e6", relief=tk.FLAT)
task_entry.pack(pady=(0, 10), ipady=8)

# Due Date Label and Date Picker
tk.Label(root, text="Due Date", font=("Helvetica", 12), bg="#1c1c1e", fg="#e4e4e6").pack(pady=(10, 5))
due_date_entry = DateEntry(root, width=20, font=("Helvetica", 10), background="#3a3a3c", foreground="white", bd=2)
due_date_entry.pack(pady=(0, 10))

# Priority Label and Dropdown
tk.Label(root, text="Priority", font=("Helvetica", 12), bg="#1c1c1e", fg="#e4e4e6").pack(pady=(10, 5))
priority_options = ["High", "Medium", "Low"]
priority_var = tk.StringVar(root)
priority_var.set("Select Priority")
priority_dropdown = ttk.Combobox(root, textvariable=priority_var, values=priority_options, font=("Helvetica", 10), state="readonly")
priority_dropdown.pack(pady=(0, 20))

# Buttons with modern style
button_frame = tk.Frame(root, bg="#1c1c1e")
button_frame.pack(pady=10)

button_style = {
    "bg": "#5e5ce6",
    "fg": "white",
    "font": ("Helvetica", 10),
    "width": 12,
    "relief": tk.FLAT,
}


add_button = tk.Button(button_frame, text="Add Task", command=add_task, **button_style)
add_button.grid(row=0, column=0, padx=5, pady=5)

delete_button = tk.Button(button_frame, text="Delete Task", command=delete_task, bg="#e34c4c", fg="white", font=("Helvetica", 10), width=12, relief=tk.FLAT)
delete_button.grid(row=0, column=1, padx=5, pady=5)

clear_button = tk.Button(button_frame, text="Clear All", command=clear_tasks, bg="#ff8a3d", fg="white", font=("Helvetica", 10), width=12, relief=tk.FLAT)
clear_button.grid(row=0, column=2, padx=5, pady=5)


# Search bar with modern style
search_frame = tk.Frame(root, bg="#1c1c1e")
search_frame.pack(pady=(20, 10))

search_entry = tk.Entry(search_frame, font=("Helvetica", 12), width=22, bg="#3a3a3c", fg="#e4e4e6", insertbackground="#e4e4e6", relief=tk.FLAT)
search_entry.grid(row=0, column=0, padx=5, ipady=8)

search_button = tk.Button(search_frame, text="Search", command=search_tasks, bg="#5e5ce6", fg="white", font=("Helvetica", 10), width=12, relief=tk.FLAT)
search_button.grid(row=0, column=1, padx=5)

# Load tasks on start
load_tasks()

# Run the main loop
root.mainloop()