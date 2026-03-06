import sys

from .models import Task, User


def main(argv=None):
    argv = list(sys.argv[1:] if argv is None else argv)

    if len(argv) < 3 or argv[0] != "add-task":
        print("Usage: python -m lib.cli_tool add-task <user> <task>")
        return 1

    _, user_name, task_title = argv[0], argv[1], " ".join(argv[2:])
    user = User(user_name)
    task = Task(task_title)
    user.add_task(task)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())