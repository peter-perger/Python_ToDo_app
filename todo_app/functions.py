import os

current_dir = os.path.dirname(__file__)

FILEPATH = os.path.join(current_dir, "todos.txt")


def get_todos(filepath=FILEPATH):
    """ Read a text file and return a list of to-do items """
    with open(filepath, 'r') as file:
        todos = file.readlines()
    return todos


def write_todos(todos_arg, filepath=FILEPATH):
    """ Write a to-do item list in the text file """
    with open(filepath, 'w') as file:
        for line in todos_arg:
            if not line.endswith('\n'):
                line = line + '\n'
            file.writelines(line)


if __name__ == "__main__":
    print(get_todos())
