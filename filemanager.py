import os
import shutil
import sys

current_path = os.getcwd()


def create_directory(name):
    new_path = os.path.join(current_path, name)
    if os.path.exists(new_path):
        message = 'Папка уже существует!'
    else:
        os.mkdir(new_path)
        message = f'Создана папка {name}'
    return message


def copy_file_or_directory(name, new_name):
    if os.path.isdir(name):
        shutil.copytree(name, new_name)
    else:
        shutil.copyfile(name, new_name)


def filenames():
    result = []
    for item in os.listdir():
        if os.path.isfile(item):
            result.append(item)
    return result


def author_info():
    return 'Leonid Orlov'


def quit():
    sys.exit(0)
