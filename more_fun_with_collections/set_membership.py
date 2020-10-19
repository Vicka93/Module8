"""
Author:Viktoria Denys
Program:set_membership.py
contains in_set function.
"""

# accepts a set and element and return a boolean value stating if the element is in the set
def in_set(some_set, some_val):

    return some_val in some_set


if __name__ == '__main__':
    my_set = {1, 2, 3, 4}
    my_val = 2
    # checking if  an item in the set
    print("Is {} in {}? {}".format(my_val,my_set,in_set(my_set, my_val)))
