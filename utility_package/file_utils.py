"""
Custom File Operations Module
"""


def create_file(filename):
    with open(filename, "x") as file:
        pass

    return True


def write_file(filename, data):
    with open(filename, "w") as file:
        file.write(data)

    return True


def read_file(filename):
    with open(filename, "r") as file:
        content = file.read()

    return content


def append_file(filename, data):
    with open(filename, "a") as file:
        file.write(data)

    return True