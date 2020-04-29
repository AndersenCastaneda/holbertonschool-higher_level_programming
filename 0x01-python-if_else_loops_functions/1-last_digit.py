#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    last = ((number * -1) % 10) * -1
else:
    last = number % 10
strline = "Last digit of {} is {}".format(number, last)
if last > 5:
    print(strline + " and is greater than 5")
if last == 0:
    print(strline + " and is 0")
if last < 6 and last != 0:
    print(strline + " and is less than 6 and not 0")
