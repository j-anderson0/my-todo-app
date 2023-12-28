import os
 
 
def get_todos():
    filepath = os.path.join(os.getcwd(), "todos.txt")
    with open(filepath, "r") as file_local:
        todos = [line.strip() for line in file_local.readlines()]
    return todos


def write_todos(todos_arg, filepath=os.path.join(os.getcwd(), "todos.txt")):
    """ Write the to-do item list in the text file."""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)