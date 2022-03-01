# My Application Overview Lesson

# This function should be lowercase and if more than one word it should have
# an underscore to separate each word. You should have a parenthesis after
# the name followed by a colon. Statements that are part of a function should
# be 4 spaces indented

def my_function():
    print('Hello')
    print('World')


# To run the function, you must call it by name.
my_function()


# When defining a function with arguments, those arguments go in between the
# parenthesis and separated by commas

def my_other(arg1, arg2):
    print(arg1)
    print(arg2)


my_other("Red", "Green")


# Variable Names
# - must start with a letter or and underscore
# - Can not begin with a number
# - Can only contain alpha-numeric character and underscores
# - Are case-sensitive

# The variables are on the left while the literal value is on the right
value = 'Blue'
value2 = 10

# Variables can even change types
value3 = 'Happy'
value3 = 20


# Multi-line statements use a backslash to continue a statement
alpha = 1 + 2 + 3 \
    + 4 + 5

# more than one variable declared
beta = 10; hello = "his"; delta = 5

up, down, left = 'town', 'ok', 'right'


# A class is an object, which is a blueprint. An instantiation of an object
# allows for all fields and functions to be accessed within. Like functions
# outside the class, you need to provide two empty spaces before it is defined.

class MyFirstClass:
    name = 'Ethan'

    # This is a method rather than a function because it is inside the class
    def something(self):
        print('Something')


my_class = MyFirstClass()
print(my_class.name)
my_class.something()
