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