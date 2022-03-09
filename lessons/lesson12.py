# Lesson 12 Exception Handling

def sample_divide():
    print('Let\'s divide two numbers.')
    try:
        first = input('The first number is? ')
        second = input('The second number is? ')
        answer = int(first) / int(second)
        print(answer)
    except (ZeroDivisionError, ValueError):
        print('You can\'t divide by zero or use words.')


# sample_divide()


def mult_except_sample():
    names = ('Dave', 'Matt', 'Jody')
    these = (25.4, '30j', 34)

    try:
        delta = int(these[3])
        echo = complex(these[0], 5)
        print('Delta is ' + str(delta))
    except IndexError:
        print('Please provide at least 1 argument')
    except ValueError:
        print('That is not a number')
    except TypeError:
        print('You have provided something weird')
    except NameError:
        print('I dunno how to calculate that')


# mult_except_sample()

# The else block can be used to execute code that does not need to be tested.
# This else will only execute if the try succeeds.
alpha, fox = 5, 10


def sample_except_else(arg):
    try:
        if fox > arg:
            golf = fox / arg
            print('Value is {}'.format(golf))
    except ZeroDivisionError:
        print('An error has occured')
    else:
        print('Division was successful')


# sample_except_else(14)


# The finally block is executed regardless of whether the try block succeeds
def sample_finally():
    try:
        if fox > alpha:
            bravo = fox / (fox - alpha) - 5
            print('Value is {}'.format(bravo))
    except ZeroDivisionError:
        print('An error occurred')
    else:
        print('else prints')
    finally:
        print('Finally prints')


sample_finally()
