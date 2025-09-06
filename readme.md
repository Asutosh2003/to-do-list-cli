📝 To-Do List (CLI)

A simple Command-Line To-Do List Application built with Python.
You can add, view, and delete tasks. Tasks are now saved in a JSON file so they persist between sessions.

📌 Features

➕ Add new tasks

👀 View all tasks

❌ Delete tasks by number

💾 Tasks are saved to tasks.json (persistence)

🎨 Colored output for better UX

🚀 How to Run

Clone this repository:

git clone https://github.com/your-username/todo-list-cli.git


Navigate into the project folder:

cd todo-list-cli


Run the program:

python main.py

📂 JSON Persistence

In the updated version, tasks are stored in a file called tasks.json.
This means your to-do list is saved even after you exit the program.

🔑 How it Works

On startup → load_task() loads tasks from tasks.json (if it exists).

On add/delete → save_task() updates tasks.json.

If the file is empty/corrupted → it resets to an empty list.

Example
$ python main.py
 ------ To Do List App  ------ 
 1. View Task
 2. Add Task
 3. Delete Task
 4. Exit

 Please Choose an option from the above :- 2
 Please enter a Task to add Finish homework
 --Task added successfully--

# After exiting, the task is saved in tasks.json

📸 Demo (Sample Output)
 ------ To Do List App  ------ 
 1. View Task
 2. Add Task
 3. Delete Task
 4. Exit

 Please Choose an option from the above :- 1
 Current Tasks :-
 1. Buy milk
 2. Finish homework
 ---- End ----

📌 Future Improvements

✅ Mark tasks as completed

✅ Add due dates

✅ Edit tasks instead of just deleting

✅ Search tasks

👨‍💻 Author

Made with ❤️ by Asutosh Samantaray