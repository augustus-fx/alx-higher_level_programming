#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    ldigit = -number % 10
    ldigit = -ldigit
else:
    ldigit = number % 10
if digit > 5:
   print("Last digit of {} is {} and is greater \
than 5".format(number, ldigit),
elif ldigit > 5:
    print("Last digit of {} is {} and is less than\
6 and not 0".format(number, ldigit))
elif ldigit == 0:
    print("Last digit of {} of {} and is 0".format(number, ldigit))
