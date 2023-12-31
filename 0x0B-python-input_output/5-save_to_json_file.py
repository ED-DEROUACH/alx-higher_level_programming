#!/usr/bin/python3
""" Module that writes an Object to a text file using
a JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """Writes a JSON representation of an object to a text file."""
    with open(filename, mode='w', encoding='utf-8') as file:
        json.dump(my_obj, file)
