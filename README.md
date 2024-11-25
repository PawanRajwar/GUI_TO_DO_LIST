# **📝 Modern To-Do List Application**

---

## **👨‍🏫 Submitted To**  
**Dr. Prateek Raj Gautam**

---

## **👨‍🎓 Submitted By**  
- **Name**: Pawan Singh Rajwar  
- **SAP ID**: 590017545  

---

## **📄 Project Title**  
**Modern To-Do List Application**

---

## **📖 Description**  
This project is a **Modern To-Do List Application** built with Python's Tkinter library. It provides a clean and functional GUI for managing daily tasks with features like **task prioritization**, **due dates**, and **search functionality**. Tasks are saved automatically, ensuring persistence across sessions, and the dark, minimalist theme enhances user experience.

---

## **✨ Key Features**
### 🧹 **Task Management**:
- Add, delete, and clear tasks in a user-friendly interface.
- Assign due dates and priority levels to tasks for better organization.

### 📂 **Automatic Persistent Storage**:
- Tasks are saved automatically in a `tasks.json` file, ensuring no data loss even after the app is closed.

### 📅 **Date and Priority Selection**:
- Select valid due dates using a **date picker widget** (`tkcalendar`).
- Assign tasks a priority level (**High, Medium, Low**) using a dropdown menu.

### 🔍 **Search Functionality**:
- Use the search bar to filter tasks by keywords, making it easy to find specific tasks.

### 🎨 **Modern and Aesthetic GUI**:
- Features a **dark, minimalist theme** with intuitive layouts and button styling for a clean and modern look.

---

## **🔧 Installation**
### Clone the repository:
```bash
git clone https://github.com/PawanRajwar/GUI_TO_DO_LIST.git

```

### Install dependencies:
```bash
pip install tkcalendar
```

### Run the application:
```bash
python modern_to_do_list.py
```

---

## **📚 Usage**
1. **Start the Application**:
   - Launch the app by running the Python script.  
   - The main window will display a list of tasks, and you can add, delete, search, or clear tasks.

2. **Add a Task**:
   - Enter a task description, select a due date using the date picker, and assign a priority level.
   - Click **Add Task** to add it to the list.

3. **Delete or Clear Tasks**:
   - Select a task in the list and click **Delete Task** to remove it.  
   - Use the **Clear All** button to remove all tasks after confirming.

4. **Search Tasks**:
   - Type a keyword in the search bar to filter tasks. Only tasks containing the keyword will appear.

5. **Persistent Storage**:
   - Tasks are automatically saved to `tasks.json` whenever you make changes.

---

## **🛠️ Libraries Used**
1. **`tkinter`**: For building the GUI.
2. **`tkcalendar`**: For the date picker widget.
3. **`json`**: For saving and loading tasks persistently.

---

## **📸 Screenshots**

### ✅ **Main Interface**
![To-do list Screenshot](<Screenshot 2024-11-25 122402-1.png>)

### 🔥 **Priority Selection**
![Priority Functionality](<Screenshot 2024-11-25 122416-1.png>)

### ✨ **Added Task Display**
![Added Task Screenshot](<Screenshot 2024-11-25 122431-1.png>)