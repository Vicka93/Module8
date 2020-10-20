"""
Author:Viktoria Denys
Program:dict_membership.py
contains in_dict function.
"""


def in_dict(some_dict, some_val):
    # accepts a dictionary and return a boolean value stating if the element is in the dictionary
    return some_val in some_dict


if __name__ == '__main__':
    my_dict = {'A': 90, 'B': 80, 'C': 70, 'D': 60, 'F': 0}
    my_val = 'A'
    # checking if  an item in the dictionary
    print("Is {} in {}? {}".format(my_val, my_dict, in_dict(my_dict, my_val)))
