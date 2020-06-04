#!/usr/bin/python3
""" Load, Add, Save Module """
import sys
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file


try:
    lst = load_from_json_file('add_item.json')
except:
    lst = []

args = sys.argv
for i in range(1, len(args)):
    lst.append(args[i])

save_to_json_file(lst, 'add_item.json')
