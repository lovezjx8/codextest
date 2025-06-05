# codextest

This repository contains a simple todo application. You can use it via the
command line or with a small graphical interface.

## Usage

Add a task:

```bash
python3 main.py add "My task"
```

List tasks:

```bash
python3 main.py list
```

Mark task as completed:

```bash
python3 main.py done 1
```

Delete a task (or all tasks):

```bash
python3 main.py delete 1 2 3   # delete tasks 1, 2 and 3
python3 main.py delete all     # delete all tasks
```

## GUI

Run the graphical interface:

```bash
python3 gui.py
```

In the window you can select tasks and use the **Complete**, **Delete** or
**Clear All** buttons to update the list.
