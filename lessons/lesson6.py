# Lesson 6 - Control Flow Statements

# Boolean
# These values are either True or False
def boolean_sample():
    print(bool('sample'))
    print(bool(0.0))


# boolean_sample()

# if statement
# Used to find out if a condition is true
def basic_if(arg1, arg2):
    if arg1 > arg2:
        print(f'{arg1} is greater than {arg2}')

    if arg1 == arg2:
        print(f'{arg1} is equal to {arg2}')


# basic_if(10, 10)

# elif example
# Used when the first condition is false, and you want to try another condition
def basic_if_elif(arg):
    if arg > 10:
        print(f'{arg} is greater than 10')
    elif arg == 10:
        print(f'{arg} is equal to 10')
    elif arg < 10:
        print(f'{arg} is less than 10')


# basic_if_elif(10)

# else statement
# This keyword can be used to execute a block of code when the if statement
# results are false
def else_example(arg):
    if arg > 15:
        print(f'{arg} is greater than 15')
    else:
        print(f'{arg} is less than 15')


# else_example(12)


# else with elif
def check_grade(arg):
    if arg == 'A':
        print('Excellent')
    elif arg == 'B':
        print('Good')
    elif arg == 'C':
        print('Average')
    elif arg == 'D':
        print('Below Average')
    elif arg == 'F':
        print('Failed')
    else:
        print('Not a valid grade')


# check_grade('d'.upper())

# Nested If Statement
# This allows an if statement to be inside another if statement.
# The inner if statement only evaluates if the outer if is true.
happy = 14


def nested_example(arg):
    if happy > arg:
        print(f'{happy} is greater than he argument')
        if arg > 5:
            print(f'{arg} is greater than 30')
        else:
            print(f'{arg} is less than 30')


# nested_example(4)

# Ternary Statement
# One condition can be performed on one line
# Basically a shorthand if statement
golf = 42
hotel = 24

# if shorthand
result = golf if golf > hotel else hotel
# print(result)

# Long form of above
# if golf > hotel:
#     print(golf)
# else:
#     print(hotel)
# print('both are equal' if golf == hotel else 'golf is greater' if golf > hotel
#       else 'hotel is greater')


# This function will break down the above shorthand to normal if
def if_short_decoded():
    if golf == hotel:
        print(f'{golf} is equal to {hotel}')
    elif golf > hotel:
        print(f'{golf} is greater than {hotel}')
    else:
        print(f'{hotel} is greater than {golf}')


# if_short_decoded()


# and & or keyword
def combined(arg1, arg2, arg3):
    if arg1 > arg2 and arg1 >= arg3:
        print('Argument 1 is greatest')

    if arg2 > arg3 or arg2 <= arg3:
        print('Argument 2 is less or equal to arg3')


# combined(30, 20, 30)
