#!/usr/bin/python3
"""Return an object attribute lookup function."""


def lookup(obj):
    """REturn a list of an object's available attributes."""
    return (dir(obj))
