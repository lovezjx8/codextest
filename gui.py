import tkinter as tk
from tkinter import messagebox
from todo import add_task, get_tasks


def refresh_tasks(listbox: tk.Listbox):
    listbox.delete(0, tk.END)
    for task in get_tasks():
        listbox.insert(tk.END, task)


def on_add(entry: tk.Entry, listbox: tk.Listbox):
    task = entry.get().strip()
    if not task:
        messagebox.showwarning("No task", "Please enter a task description")
        return
    add_task(task)
    entry.delete(0, tk.END)
    refresh_tasks(listbox)


def main():
    root = tk.Tk()
    root.title("Todo List")

    frame = tk.Frame(root)
    frame.pack(padx=10, pady=10)

    entry = tk.Entry(frame, width=40)
    entry.pack(side=tk.LEFT)

    listbox = tk.Listbox(root, width=50)
    listbox.pack(padx=10, pady=(5, 10))

    add_button = tk.Button(
        frame,
        text="Add",
        command=lambda: on_add(entry, listbox)
    )
    add_button.pack(side=tk.LEFT, padx=(5, 0))

    refresh_tasks(listbox)

    root.mainloop()


if __name__ == "__main__":
    main()
