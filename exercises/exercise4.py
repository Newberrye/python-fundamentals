# 1. page 29
print('#1 Problem')
# 2-8 Number Eight
print(3 + 5)
print(10 - 2)
print(4 * 2)
print(int(8 / 1))

# 2-9 Favorite Number
favourite_number = 7
message = f'My favorite number is {favourite_number}!'
print(message)

# 2. Assign variables to following sets of numbers. Use underscores to make
# them more readable. Write a function called number_sets and print each
# variable inside the function. Call all the function to verify your
# results.
# a.456234
# b.68423791
# c.13794628
# d.96374
print('#2 Problem')
numbera = 456_234
numberb = 68_423_791
numberc = 13_794_628
numberd = 96_374


def number_sets():
    print(numbera)
    print(numberb)
    print(numberc)
    print(numberd)


number_sets()
print()

# 3. Write a function that will take 2 arguments. Using Type conversion,
# convert the first argument from int to float. Convert the second argument
# from float to int. Call the function and provide the correct values for
# each argument to verify your results. One argument should be a float and
# the other an int.
print('#3 Problem')


# Added a print to see the change since directions did not  directly ask for it.
def number_converter(number_int, number_flo):
    print(float(number_int))
    print(int(number_flo))


number_converter(4, 5.67)
print()

# 4. Write a function that will have two inputs. The first input method
# should ask “What is your favorite movie” the second input method should ask
# “How many times have you seen it?”. The second input should be inside an
# int function. Each input method should be assigned to a variable. In a print
# statement using placeholders, the output result should be “I have seen {
# favorite movie} {number of times} times”.
print('#4 Problem')


def input_message():
    message1 = 'What is your favourite movie? '
    message2 = 'How many times have you seen it? '

    response1 = input(message1)
    response2 = int(input(message2))

    # Using .format to practice more rather than f''
    answer = 'I have seen {0} {1} times.'
    print(answer.format(response1, response2))


input_message()
print()
