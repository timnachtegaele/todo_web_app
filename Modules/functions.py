FILEPATH = 'todos.txt'


def get_write_todos(action, todos_local='', filepath_loc=FILEPATH):
    """ Function used to read and write from/to txt files. """
    match action:
        case 'r':
            with open(filepath_loc, action) as file:
                todos_local = file.readlines()
        case 'w':
            with open(filepath_loc, action) as file:
                file.writelines(todos_local)
    return todos_local


if __name__ == "__main__":
    print(get_write_todos('r', '', '../files/todos.txt'))