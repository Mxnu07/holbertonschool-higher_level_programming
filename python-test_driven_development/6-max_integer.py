#!/usr/bin/python3
"""Module for max_integer"""
def max_integer(list=[]):
    """Function to find the max integer in a list"""
    if len(list) == 0:
        return None
    max = list[0]
    for i in list:
        if i > max:
            max = i
    return max
