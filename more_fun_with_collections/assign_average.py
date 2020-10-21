"""
Author:Viktoria Denys
Program:assign_average.py
function accepts entry and return value from dictionary. if non-key passed statement from
my_dict.get() function will be returned
"""

# function accepts entry and return a value from dictionary
def switch_average(entry):
    # created a dictionary for grades and statements
    my_dict = {'A': "You entered an A",
               'B': "You entered an B",
               'C': "You entered an C",
               'D': "You entered an D",
               'F': "You entered an F"}
    # if a non-key is passed , it will return a statement below ""{entry} is not a valid Grade".format(entry.upper()"
    result = my_dict.get(entry.upper(), "{} is not a valid Grade".format(entry.upper()))
    return result


if __name__ == '__main__':
    print(switch_average('g'))
