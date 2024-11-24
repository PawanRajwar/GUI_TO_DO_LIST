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

### 2. Automatic Data Handling:
- Loading Tasks: The load_tasks() function reads data from tasks.json upon startup. If the file doesn’t exist or is empty, an empty list is initialized.

- Saving Tasks: The save_tasks() function automatically writes the current task list to tasks.json each time a task is added, deleted, or cleared, ensuring tasks are consistently saved.

### 3. Task Addition:
- Add Task: Users enter a task description in the entry box and can then select a due date and priority level. The app verifies that a task name, valid due date, and priority level are entered before adding it.

- Due Date Picker: The DateEntry widget from tkcalendar allows users to pick only valid dates.

- Priority Dropdown: Users select a priority level (High, Medium, Low) from a dropdown menu, allowing for organized task sorting.

### 4. Task Deletion and Clear Functionality:
- Delete Task: A task selected in the Listbox can be deleted by clicking "Delete Task." This action updates the Listbox display and automatically saves changes.

- Clear All Tasks: The "Clear All" button removes all tasks after confirming, ensuring that no data is accidentally cleared.

### 5. Search Functionality:
- The search entry box allows users to filter tasks by entering keywords. The search_tasks() function compares the input with each task description, updating the Listbox to show only matching tasks.

### 6. Button Styling and Layout:
- Buttons are grouped within frames to maintain a clean and organized layout.

- Buttons are styled with a modern look, using specific colors and fonts consistent with the app’s theme.

- Add Task, Delete Task, Clear All, and Search buttons provide intuitive access to the main features.

## Requirements
- Python 3.x

- tkinter (included with Python)

- tkcalendar: Install this package by running pip install tkcalendar.