# I will be switching coding formats a lot during this exercise to practice
# different styles and see how they look in the editor

# 1. On page 78 of your book, do 5-1 of the Try it Yourself. Put all your code
# in your exercise5.py file.
print('#1 Problem')
car, test1, num, test2, alice, test3 = 'Ford', 'ford', 2, '2', 90, -127
a, test4, b, test5, c, test6, d, test7 = 'hello', 'HELLO', 1, 0, -1, -2, 4, 5
e, test8, f, test9, g, test10 = '23', 23, 55, 55, ' space ', 'space'


def print_tests():
    print('Is Ford == ford? I predict false!')
    print(car == test1)

    print('Is 2 == \'2\'? I predict false!')
    print(num == test2)

    print('Is 90 >= -127? I predict true!')
    print(alice >= test3)

    print('Is hello == HELLO.lower()? I predict true.')
    print(a == test4.lower())

    print('Is 1 < 0? I predict false.')
    print(b < test5)

    print('Is -1 > -2? I predict true.')
    print(c > test6)

    print('Is 4 <= 5? I predict true')
    print(d <= test7)

    print('Is \'23\'==23? I predict false.')
    print(e == test8)

    print('Is 55==55? I predict true.')
    print(f == test9)

    print('Is  space  == space? I predict false cause of extra space.')
    print(g == test10)


print_tests()
print()
# 2. On page 78 of your book, create new examples that meet the bullet points
# of 5-2. Put your code for this in your exercise5.py file.
print('#2 Problem')

# String equality, inequality, and .lower
string1 = 'Peanut'; string2 = 'peanut'
print('Is Peanut == peanut? I predict false')
print(string1 == string2)
print('Is Peanut != peanut? I predict true')
print(string1 != string2)
print('Is Peanut.lower() == peanut.lower(). I predict true')
print(string1.lower() == string2.lower())

# Numbers Greater than, Less than, greater than or equal, and less than or equal
num1, num2, num3, = 3.0, 3, 5
print('Is 3.0 > 3? I predict false')
print(num1 > num2)
print('Is 5 < 3? I predict false')
print(num3 < num2)
print('Is 3 >= 3.0? I predict true')
print(num2 >= num1)
print('Is 3 <= 5? I predict true')
print(num2 <= num3)

# And Or
numb1 = 5; numb2 = 6; numb3 = 9
print('Is 6 > 5 AND 6 > 9? I predict false')
print(numb2 > numb1 and numb2 > numb3)
print('Is 6 > 5 OR 6 > 9? I predict true')
print(numb2 > numb1 or numb2 > numb3)

# Lists: in, not in
my_list = ['never', 'gonna', 'give', 'you', 'down']
phrase = 'give'
print(f'{my_list}\nIs {phrase} in my list? I predict true')
print(phrase in my_list)
print('{0}\nIs {1} not in my list? I predict false'.format(my_list, phrase))
print(phrase not in my_list)

print()
# 3. Write a function that will take 2 arguments. Inside the function provide
# examples of all the arithmetic operators. Provide a variable for each
# solution and print the results of each.
print('#3 Problem')


def calc_operators(value1, value2):
    addition = value1 + value2
    subtraction = value1 - value2
    multiplication = value1 * value2
    division = value1 / value2
    floor_division = value1 // value2
    exponents = value1 ** value2
    modulus = value1 % value2

    print(f'Numbers: {value1} operator {value2}')
    print(f'Addition: {addition}')
    print(f'Subtraction: {subtraction}')
    print(f'Multiplication: {multiplication}')
    print(f'Division: {division}')
    print(f'Floor: {floor_division}')
    print(f'Exponents: {exponents}')
    print(f'Modulus: {modulus}')


calc_operators(100, 5)
print()
# 4. Write a function that takes only 1 argument. Inside the function provide
# examples of Assignment operators: modulus equals, minus equals, exponent
# equals & plus equals. Provide a variable for each solution and print the
# results of each.
print('#4 Problem')


def assignment_operator(value):
    modulus = value
    minus = value
    exponent = value
    plus = value
    mo = '%='
    mi = '-='
    ex = '**='
    pl = '+='
    message = '{0}: {1}'

    modulus %= value
    minus -= value
    exponent **= value
    plus += value

    print(f'Number: {value} assignment operator {value}')
    print(message.format(mo, modulus))
    print(message.format(mi, minus))
    print(message.format(ex, exponent))
    print(message.format(pl, plus))


assignment_operator(10)
