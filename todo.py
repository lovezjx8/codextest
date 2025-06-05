import json
from pathlib import Path

data_file = Path(__file__).with_name('data.json')

def load_tasks():
    """Load tasks from the data file and convert legacy formats."""
    if not data_file.exists():
        return []

    with open(data_file, 'r', encoding='utf-8') as f:
        tasks = json.load(f).get('tasks', [])

    # Convert from list of strings to list of dicts with completion info
    converted = []
    needs_save = False
    for item in tasks:
        if isinstance(item, str):
            converted.append({'description': item, 'completed': False})
            needs_save = True
        elif isinstance(item, dict):
            converted.append(
                {
                    'description': item.get('description', ''),
                    'completed': bool(item.get('completed', False)),
                }
            )
        else:
            needs_save = True

    if needs_save:
        save_tasks(converted)

    return converted

def save_tasks(tasks):
    with open(data_file, 'w', encoding='utf-8') as f:
        json.dump({'tasks': tasks}, f, indent=2)

def add_task(description: str):
    tasks = load_tasks()
    tasks.append({'description': description, 'completed': False})
    save_tasks(tasks)


def complete_task(index: int):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        tasks[index]['completed'] = True
        save_tasks(tasks)


def delete_tasks(indices):
    """Delete tasks by a list of zero-based indices."""
    tasks = load_tasks()
    for idx in sorted(set(indices), reverse=True):
        if 0 <= idx < len(tasks):
            tasks.pop(idx)
    save_tasks(tasks)


def clear_tasks():
    save_tasks([])

def get_tasks():
    """Return the list of tasks from the data file."""
    return load_tasks()


def list_tasks():
    """Print the list of saved tasks to the console."""
    tasks = get_tasks()
    for i, task in enumerate(tasks, 1):
        status = "[x]" if task.get('completed') else "[ ]"
        print(f"{i}. {status} {task.get('description')}")
