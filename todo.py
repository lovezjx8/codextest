import json
from pathlib import Path

data_file = Path(__file__).with_name('data.json')

def load_tasks():
    if data_file.exists():
        with open(data_file, 'r', encoding='utf-8') as f:
            return json.load(f).get('tasks', [])
    return []

def save_tasks(tasks):
    with open(data_file, 'w', encoding='utf-8') as f:
        json.dump({'tasks': tasks}, f, indent=2)

def add_task(task):
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)

def list_tasks():
    tasks = load_tasks()
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")
