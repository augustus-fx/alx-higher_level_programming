#!/usr/bin/python3

def safe_print_integer(value):
    """Print an integer with {:d}".format().

    Args:
	value (int): The integer to print.

    Returns:
	If a TypeError or valueError occurs - Flase.
	Otherwise - True
    """
   Try:
	print("{:d}".format(value))
	return (True)
   except (TypeError. valueError):
