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
