#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        div = a / b
        print("Inside result: {}".format(div))
    except:
        print("Inside result: {}".format(None))
