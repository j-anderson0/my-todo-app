FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    """Read a text file and return the list of to-do items."""
    try:
        with open(filepath, 'r') as file_local:
            todos_local = file_local.readlines()
    except FileNotFoundError:
        # If the file doesn't exist, create it and return an empty list
        todos_local = []
        with open(filepath, 'w') as file_local:
            pass
    return todos_local

def write_todos(todos_arg, filepath=FILEPATH):
    """Write the to-do item list to the text file."""
    with open(filepath, 'w') as file:
        # Ensure each todo item ends with a newline character
        for todo in todos_arg:
            if not todo.endswith('\n'):
                todo += '\n'
            file.write(todo)

# Example usage
# todos = get_todos()
# todos.append('New Todo Item\n')
# write_todos(todos)