#!/usr/bin/python3
"""Defines a JSON file-reading function."""
import json


def load_from_json_file(filename):
    """Create a Pyhton object from a JSON file.
    Args:
        filename (str): String representation of an aobject

    Returns:
        None
    """
    with open(filename) as f:
        obj_frm_json = json.loads(file.read())

    return obj_frm_json
