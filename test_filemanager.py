import os
from filemanager import author_info, create_directory
from victory import date_to_str


def test_autor():
    assert author_info() == 'Leonid Orlov'


def test_victory():
    assert date_to_str('20.10.1973')


def test_create_dir():
    name = 'test_dir'
    assert create_directory(name) == 'Создана папка {name}'
    assert create_directory(name) == 'Папка уже существует!'
    os.rmdir(name)
