# 1.On page 84of your book, do 5-3of the Try it Yourself. Put all your code
# in your exercise6.py file.
print('#1')
alien_color = 'red'

# Fails
if alien_color == 'green':
    print('Player has just gained 5 points!')

# Passes
if alien_color == 'red':
    print('Player has earned 5 points!')

print()
# 2.On page 84 of your book, do 5-4 of the Try it Yourself. Put all your code
# in your exercise6.py file.
print('#2')
alien_color = 'yellow'

# Else passes
if alien_color == 'green':
    print('Player has earned 5 points for hitting green!')
else:
    print('You did not kill a green alien and earned 10 points!')

# If passes
if alien_color == 'yellow':
    print('Player has earned 5 points for hitting yellow!')
else:
    print('You did not kill a yellow alien and earned 10 points!')

print()
# 3.On page 84 of your book, do 5-5 of the Try it Yourself. Put all your code
# in your exercise6.py file.
print('#3')

# Green Passes
alien_color = 'green'
if alien_color == 'green':
    print('+5 points')
elif alien_color == 'yellow':
    print('+10 points')
elif alien_color == 'red':
    print('15 points')

# Yellow Passes
alien_color = 'yellow'
if alien_color == 'green':
    print('+5 points')
elif alien_color == 'yellow':
    print('+10 points')
elif alien_color == 'red':
    print('15 points')

# Red Passes
alien_color = 'red'
if alien_color == 'green':
    print('+5 points')
elif alien_color == 'yellow':
    print('+10 points')
elif alien_color == 'red':
    print('+15 points')

print()
# 4.On page 84 of your book, do 5-6 of the Try it Yourself. Put all your code
# in your exercise6.py file.
print('#4')
age = 90

# Will be using and operator & shorthand
if age < 2:
    print('Whose a cute baby!')
elif 2 <= age < 4:
    print('You are a toddler.')
elif age >= 4 and age < 13:
    print('You are a kid.')
elif age >= 13 and age < 20:
    print('You are a teenager.')
elif 20 <= age < 65:
    print('You are an adult')
elif age >= 65:
    print('Elder One')

print()
# 5.Write a function that takes an argument. Check this argument to see if it
# is a Boolean using the bool method. Call the method and use the below
# values as your argument. Using comments, provide the name of the argument
# and if it was true or false from running the code.
print('#5')
# There we no values listed below, so I created some values to test:

# Argument values
# 0.0 - False
# 0 - False
# None - False
# False - False
# True - True
# 1 - True
# '' - False
# ' ' - True
# 'Hello World' - True
# ' Hello World' - True
# 5 > 10 - False
# 5 > 3 - True


def check_boolean(arg):
    print(bool(arg))


check_boolean(5 > 3)
