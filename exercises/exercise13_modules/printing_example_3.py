"""This program prints multiple lines of text using printing_function.py
module."""
from printing_functions import print_stuff
# Most specific function is used.
# If there were more functions in the file, they would not be imported


def adding_numbers(
        parameter_0, parameter_1, parameter_2,
        parameter_3, parameter_4, parameter_5,
        parameter_6='6'):
    """Parameters are turned into integers and are added together"""
    num1 = int(parameter_0)
    num2 = int(parameter_1)
    num3 = int(parameter_2)
    num4 = int(parameter_3)
    num5 = int(parameter_4)
    num6 = int(parameter_5)
    num7 = int(parameter_6)

    added = num1 + num2 + num3 + num4 + num5 + num6 + num7
    return added


added_numbers = adding_numbers('1', '2', '3', '4', '5', '6')
print_stuff(added_numbers)




