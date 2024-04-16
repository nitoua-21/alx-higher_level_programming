#!/usr/bin/python3
"""Module to add all arguments to a Python list,
    and then save them to a file
"""


import sys
from os import path


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

args = sys.argv[1:]
filename = 'add_item.json'

if path.exists(filename):
    my_list = load_from_json_file(filename)
else:
    my_list = []

my_list.extend(args)
save_to_json_file(my_list, filename)
