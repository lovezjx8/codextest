import tkinter as tk
from tkinter import messagebox, simpledialog
from todo import (
    add_task,
    complete_task,
    delete_tasks,
    edit_task,
    clear_tasks,
    get_tasks,
)


def refresh_tasks(listbox: tk.Listbox):
    listbox.delete(0, tk.END)
    for task in get_tasks():
        prefix = "✓ " if task.get("completed") else "  "
        listbox.insert(tk.END, f"{prefix}{task.get('description')}")


def on_add(entry: tk.Entry, listbox: tk.Listbox):
    task = entry.get().strip()
    if not task:
        messagebox.showwarning("No task", "Please enter a task description")
        return
    add_task(task)
    entry.delete(0, tk.END)
    refresh_tasks(listbox)


def on_complete(listbox: tk.Listbox):
    indices = listbox.curselection()
    for idx in indices:
        complete_task(idx)
    refresh_tasks(listbox)


def on_delete(listbox: tk.Listbox):
    indices = listbox.curselection()
    delete_tasks(indices)
    refresh_tasks(listbox)


def on_edit(listbox: tk.Listbox):
    indices = listbox.curselection()
    if len(indices) != 1:
        messagebox.showwarning("Select one", "Please select a single task to edit")
        return
    idx = indices[0]
    current = get_tasks()[idx].get("description", "")
    new_desc = simpledialog.askstring("Edit Task", "Update task description", initialvalue=current)
    if new_desc is None:
        return
    new_desc = new_desc.strip()
    if new_desc:
        edit_task(idx, new_desc)
        refresh_tasks(listbox)


def on_clear(listbox: tk.Listbox):
    if messagebox.askyesno("Clear all", "Delete all tasks?"):
        clear_tasks()
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
        text="添加",
        command=lambda: on_add(entry, listbox)
    )
    add_button.pack(side=tk.LEFT, padx=(5, 0))

    complete_button = tk.Button(
        frame,
        text="完成",
        command=lambda: on_complete(listbox)
    )
    complete_button.pack(side=tk.LEFT, padx=(5, 0))

    delete_button = tk.Button(
        frame,
        text="删除",
        command=lambda: on_delete(listbox)
    )
    delete_button.pack(side=tk.LEFT, padx=(5, 0))

    edit_button = tk.Button(
        frame,
        text="编辑",
        command=lambda: on_edit(listbox)
    )
    edit_button.pack(side=tk.LEFT, padx=(5, 0))

    clear_button = tk.Button(
        frame,
        text="清空",
        command=lambda: on_clear(listbox)
    )
    clear_button.pack(side=tk.LEFT, padx=(5, 0))

    refresh_tasks(listbox)

    root.mainloop()


if __name__ == "__main__":
    main()
