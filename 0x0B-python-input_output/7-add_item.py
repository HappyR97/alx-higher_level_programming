#!/usr/bin/python3

"""

This module defines a function that adds all arguments
to a Python list and save them to a file

"""

import sys


save_to_json = __import__('5-save_to_json_file').save_to_json_file
load_from_json = __import__('6-load_from_json_file').load_from_json_file


def add_item(args):
    """Adds all arguments to a Python list and
    save them to a file"""
    my_list = []
    try:
        my_list = load_from_json('add_item.json')
    except FileNotFoundError:
        my_list = []

    my_list.extend(args)
    save_to_json(my_list, 'add_item.json')


add_item(sys.argv[1:])
