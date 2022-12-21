#!/usr/bin/python3

import sys


def safe_print_integer_err(value):
    """Prints an integer with "{:d}".format().
    If a ValueError message is caught, a corresponding
    message is printed to standard error.
    Args:
	value (int): The integer to pring.
    Returns:
	If a TypeError or ValueError occurs - False.
	Otherwise - True.
    """
    try:
        print("{:d}".format(value)
	return (True)
    except (TypeError, ValueError):
	print("Exception: {}".format(sys.exec_info()[1]), file=sys.stdrr)
	return (False)
