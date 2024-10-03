import tkinter as tk
from tkinter import messagebox, ttk

#mainwindow
root = tk.Tk()
root.title("Tiffie's todo list")
root.geometry("400x450")
root.configure(background="#abdbe3")

#Entrywidget
enter_task = tk.Entry(root, width=45)
enter_task.pack(pady=5)

#lsitbox
list_box = tk.Listbox(root, width=50, height=10, font=('Arial', 16))
# list_box.scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL)
# list_box.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
list_box.pack(pady=5)
list_box.configure(background="#abdbe3")


#CreateTask
def add_task():
    task = enter_task.get()
    if task!= "":
        list_box.insert(tk.END, task)
        entry_task.delete(0, tk.END)
    else:
        messagebox.showinfo("Error", "Nog een keer")

#Knop
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(pady=5)


#Deletetask
def delete_task():
    try:
        selected_task_index = list_box.curselection()

        if selected_task_index:
            list_box.delete(selected_task_index)
        else:
            messagebox.showinfo("Error", "Select task")
    except:
        messagebox.showinfo("Error", "Nog een keer")

#knop
delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.pack(pady=5)

#clear
def clear_task():
    list_box.delete(0, tk.END)
#knoop
clear_knop = tk.Button(root, text="Clear Task", command=clear_task)
clear_knop.pack(pady=5)


def mark_completed():
    selected_task_index = list_box.curselection()
    if selected_task_index:
        selected_task = list_box.get(selected_task_index)

        if selected_task.startswith("[✓]"):
            messagebox.showinfo("Info", "TASK COMPLETED")
        else:
            completed_task = f"[✓] {selected_task}"

            list_box.delete(selected_task_index)
            list_box.insert(selected_task_index, completed_task)
    else:
        messagebox.showinfo("Error", "SELECT TASK")

button_complete = tk.Button(root, text="Mark Completed", command=mark_completed)
button_complete.pack(pady=5)

root.mainloop()

