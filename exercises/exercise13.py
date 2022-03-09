# We have never done printing_models.py for 8.15 in problem 1. I made a bare
# minimum files to do it.

# Write functions for each of the items below. Call the function to ensure
# the results are correct.
# 1.On page 155 of your book, do 8-15 through 8-17 of the Try it Yourself.
# Put all your code in your exercise13.py file.
print('#1 Problem')
# 8-15. Printing Models: Put the functions for the example printing_models.py
# in a separate file called printing_functions.py. Write an import statement
# at the top of printing_models.py, and modify the file to use the imported
# functions.
print('8.15 Printing Models')


def print_from_module():
    """Prints stuff using printing_functions module"""
    from exercises.exercise13_modules import printing_functions

    printing_functions.print_stuff('hello')


print_from_module()

print()

# 8-16. Imports: Using a program you wrote that has one function in it,
# store that function in a separate file. Import the function into your main
# program file, and call the function using each of these approaches:
# - import module_name
# - from module_name import function_name
# - from module_name import function_name as fn
# - import module_name as mn
# - from module_name import *
print('8.16 Imports')


def module_import():
    from exercises.exercise13_modules import printing_functions

    printing_functions.print_stuff('- Import Module Name')


def from_module_import():
    from exercises.exercise13_modules.printing_functions import print_stuff

    print_stuff('- from module_name import function_name')


def from_module_import_alias():
    from exercises.exercise13_modules.printing_functions import print_stuff \
        as ps

    ps('- from module_name import function_name as fn')


def module_import_alias():
    from exercises.exercise13_modules import printing_functions as pf

    pf.print_stuff('- import module_name as mn')


# def from_module_import_all():
#     from printing_functions import *
#     print_stuff('- from module_name import *')


module_import()
from_module_import()
from_module_import_alias()
module_import_alias()
# from_module_import_all()
print('- import * gives SyntaxError: import * only allowed at module level')
print()

# 8-17. Styling Functions: Choose any three programs you wrote for this
# chapter, and make sure they follow the styling guidelines described in this
# section.
print('8.17 Styling Functions')
# Taken from files printing_function.py, printing_models.py,
# and printing_example3.py


def printing_function():
    """This function prints stuff to the user"""

    def print_stuff(arg):
        """Prints arg"""
        print(arg)


def printing_models():
    """Prints stuff using printing_functions module"""
    from exercises.exercise13_modules import printing_functions

    printing_functions.print_stuff('hello')


def printing_example_3():
    """This program prints multiple lines of text using printing_function.py
    module."""
    from exercises.exercise13_modules.printing_functions import print_stuff
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


# printing_function prints nothing since it is a module
printing_function()
printing_models()
printing_example_3()
print('\n')


# 2.On page 180 of your book, do 9-10 through 9-12 of the Try it Yourself.
# Put all your code in your exercise13.py file.
print('#2 Problem')
# 9-10. Imported Restaurant: Using your latest Restaurant class, store it in
# a module. Make a separate file that imports Restaurant. Make a Restaurant
# instance, and call one of Restaurant’s methods to show that the import
# statement is working properly.
print('9.10 Imported Restaurant')


def restaurant_import():
    """Imports Restaurant Class from exercise11 and makes an object."""
    from exercises.exercise13_modules.restaurant import Restaurant

    krusty_krabs = Restaurant('Krusty Krabs', 'Fast Food')

    krusty_krabs.describe_restaurant()
    krusty_krabs.open_restaurant()


restaurant_import()
print()

# 9-11. Imported Admin: Start with your work from Exercise 9-8 (page 173).
# Store the classes User, Privileges, and Admin in one module. Create a
# separate file, make an Admin instance, and call show_privileges() to show
# that everything is working correctly.
print('9.11 Imported Admin')


def admin_user_privileges_import():
    """Imports Classes and makes an instance of Admin"""
    from exercise13_modules.imported_admin import Admin

    admin = Admin('Admin', 'Admin', '7', 'Watching', 'White', '404')

    admin.privileges.show_privileges()


admin_user_privileges_import()
print()

# 9-12. Multiple Modules: Store the User class in one module, and store the
# Privileges and Admin classes in a separate module. In a separate file,
# create an Admin instance and call show_privileges() to show that everything
# is still working correctly
print('9.12 Multiple Modules')


def multiple_modules():
    """Imports from multiple modules and creates Admin instance"""
    import exercise13_modules.admin_privileges as ap

    admin2 = ap.Admin('Dr', 'Strange', '???', 'Also ???', 'Brown', 'Infinite')

    admin2.privileges.show_privileges()


multiple_modules()
print('\n')


# 3.On page 181 of your book, do 9-16 of the Try it Yourself. Put all your
# code in your exercise13.py file.
print('#3 Problem')
# 9-16. Python Module of the Week: One excellent resource for exploring the
# Python standard library is a site called Python Module of the Week. Go to
# https://pymotw.com/ and look at the table of contents. Find a module that
# looks interesting to you and read about it, perhaps starting with the
# random module.
print('9.16 Python Module of the Week')


def module_random():
    """Imports random module and goes through different stuff in it"""
    import random

    # random - 0 to 1.0
    for number in range(4):
        print(1 * random.random(), end=' ')
    print()

    # uniform - range
    for number in range(4):
        print(1 * random.uniform(1, 10), end=' ')
    print()

    # randint - random integers
    for number in range(4):
        print(1 * random.randint(1, 10), end=' ')
    print()

    # randrange - random integers with a step
    for number in range(4):
        print(1 * random.randrange(1, 100, 10), end=' ')
    print()

    # seeding - Controls first value in calculating random
    random.seed(10)
    for number in range(4):
        print(1 * random.random(), end=' ')
    print()


module_random()
