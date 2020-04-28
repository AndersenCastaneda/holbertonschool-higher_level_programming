#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
strline = "Last digit of {} is {}".format(number, number % 10)
if number % 10 > 5:
    print(strline + " and is greater than 5")
if number % 10 == 0:
    print(strline + " and is 0")
if number % 10 < 6 and number % 10 != 0:
    print(strline + " and is less than 6 and not 0")
