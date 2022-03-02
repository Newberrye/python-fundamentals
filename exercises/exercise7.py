# Write functions for each of the items below. Call the function to ensure
# the results are correct.

# 1.On page 60of your book, do 4-3of the Try it Yourself. Put all your code
# in your exercise7.py file.
# 4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20,
# inclusive.
print('#1 Problem: 4.3 Counting to Twenty')


def count_twenty():
    counter = 1

    #
    while counter <= 20:
        print(counter)
        counter += 1


count_twenty()

print()

# 2.On page 60 of your book, do 4-6 of the Try it Yourself. Put all your code
# in your exercise7.py file.
# 4-6. Odd Numbers: Use the third argument of the range() function to make a
# list of the odd numbers from 1 to 20. Use a for loop to print each number
print('#2 Problem 4.6 Odd Numbers')


def count_twenty_odd():
    # Using books example for creating a list.
    count_list = [count for count in range(1, 20, 2)]

    print(count_list)


count_twenty_odd()

print()

# 3.On page 60 of your book, do 4-7 of the Try it Yourself. Put all your code
# in your exercise7.py file.
# 4-7. Threes: Make a list of the multiples of 3 from 3 to 30. Use a for loop to
# print the numbers in your list.
print('#3 Problem 4.7')


def count_thirty_threes():
    count_list = []

    # Range end set to 31 to include 30; using .append just to remember this
    # method.
    for count in range(3, 31, 3):
        count_list.append(count)

    for number in count_list:
        print(number)


count_thirty_threes()

print()

# 4.On page 60 of your book, do 4-8 of the Try it Yourself. Put all your code
# in your exercise7.py file.
# 4-8. Cubes: A number raised to the third power is called a cube. For
# example, the cube of 2 is written as 2**3 in Python. Make a list of the
# first 10 cubes (that is, the cube of each integer from 1 through 10),
# and use a for loop to print out the value of each cube.
print('#4 Problem 4.8')


def count_cubes():
    cube_list = [count**3 for count in range(1, 11)]

    for number in cube_list:
        print(number)


count_cubes()
