import argparse
from todo import add_task, list_tasks
from gui import main as gui_main


def main():
    parser = argparse.ArgumentParser(description='Simple todo CLI')
    subparsers = parser.add_subparsers(dest='command')

    add_parser = subparsers.add_parser('add', help='Add a new task')
    add_parser.add_argument('task', help='Task description')

    subparsers.add_parser('list', help='List tasks')
    subparsers.add_parser('gui', help='Launch the graphical interface')

    args = parser.parse_args()

    if args.command == 'add':
        add_task(args.task)
    elif args.command == 'list':
        list_tasks()
    elif args.command == 'gui' or args.command is None:
        gui_main()
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
