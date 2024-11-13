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
