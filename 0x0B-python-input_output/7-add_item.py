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

try:
    existing_content = load_from_json_file(filename)
except FileNotFoundError:
    existing_content = []

save_to_json_file(existing_content + sys.argv[1:], filename)
