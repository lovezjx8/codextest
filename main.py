import argparse
from todo import (
    add_task,
    list_tasks,
    complete_task,
    delete_tasks,
    clear_tasks,
    edit_task,
)
from gui import main as gui_main


def main():
    parser = argparse.ArgumentParser(description='Simple todo CLI')
    subparsers = parser.add_subparsers(dest='command')

    add_parser = subparsers.add_parser('add', help='Add a new task')
    add_parser.add_argument('task', help='Task description')

    subparsers.add_parser('list', help='List tasks')

    done_parser = subparsers.add_parser('done', help='Mark a task as completed')
    done_parser.add_argument('index', type=int, help='Task number (1-based)')

    del_parser = subparsers.add_parser('delete', help='Delete tasks')
    del_parser.add_argument('indices', nargs='+', help='Task numbers or "all"')

    edit_parser = subparsers.add_parser('edit', help='Edit an existing task')
    edit_parser.add_argument('index', type=int, help='Task number (1-based)')
    edit_parser.add_argument('description', help='New task description')

    subparsers.add_parser('gui', help='Launch the graphical interface')

    args = parser.parse_args()

    if args.command == 'add':
        add_task(args.task)
    elif args.command == 'list':
        list_tasks()
    elif args.command == 'done':
        complete_task(args.index - 1)
    elif args.command == 'delete':
        if len(args.indices) == 1 and args.indices[0].lower() == 'all':
            clear_tasks()
        else:
            delete_tasks([int(i) - 1 for i in args.indices])
    elif args.command == 'edit':
        edit_task(args.index - 1, args.description)
    elif args.command == 'gui' or args.command is None:
        gui_main()
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
