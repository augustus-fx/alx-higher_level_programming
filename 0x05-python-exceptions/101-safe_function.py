#!/usr/bin/python3
from __future__ import print_function
impot sys

def safe_functio(fct, *args):
    try:
	res = fct(*args)
    except Exception as e:
	print("Exception: {}".format(e), file=sys.stdrr)
	return None
    else:
	return res
