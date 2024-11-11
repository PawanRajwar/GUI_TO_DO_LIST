# Modern To-Do List Application
This project is a Modern To-Do List Application built with Python's Tkinter GUI toolkit. The app provides a clean, minimalist, and functional user interface for managing daily tasks, organizing them by priority, and setting due dates. This README file offers a comprehensive overview of the app’s functionality, design choices, and code structure.

## Key Features

### 1. Task Management:
- Add, delete, and clear tasks easily within a user-friendly interface.

- Each task includes an optional due date and priority level, making it simple to organize tasks based on deadlines and importance.

### 2. Automatic Persistent Storage:
- Tasks are saved to a tasks.json file automatically whenever a task is added, deleted, or cleared. This ensures that all tasks are saved immediately and will persist even after the application is closed, without needing a manual save button.

### 3. Date and Priority Selection:
- Each task can include a due date, which is selected from a date picker widget (tkcalendar). This ensures only valid dates are entered.

- Tasks can also be assigned one of three priority levels: High, Medium, or Low, using a dropdown menu to make organization clearer.

### 4. Search Functionality:
- The search bar enables users to filter tasks based on keywords, making it easy to locate specific tasks within a large list.

### 5. Modern and Aesthetic GUI:
- The interface features a dark, minimalist theme with contrasting button colors for a sleek, modern look. It is optimized for readability and usability, with a consistent color scheme throughout the app.


## Code Structure and Explanation

### 1. Main Interface:
- Window Initialization: The main window is set up using Tkinter, with custom dimensions and a dark-themed color scheme for aesthetics.

- Listbox: A Listbox widget displays the list of tasks. Each entry shows the task text, due date, and priority, providing an overview of all tasks. A scrollbar is added for convenience when there are many tasks.