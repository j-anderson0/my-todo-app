FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    """ Get the to-do item list from the text file."""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ Write the to-do item list in the text file."""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)