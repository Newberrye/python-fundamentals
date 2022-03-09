# Function calls are not timed out, they will all run in order when code is ran.

# Write functions for each of the items below. Call the function to ensure
# the results are correct.
# 1.On page 201 of your book, do  through 10-6 of the Try it Yourself. Put
# all your code in your exercise12.py file.
print('#1 Problem')
# 10-6. Addition: One common problem when prompting for numerical input
# occurs when people provide text instead of numbers. When you try to convert
# the input to an int, you’ll get a ValueError. Write a program that prompts
# for two numbers. Add them together and print the result. Catch the
# ValueError if either input value is not a number, and print a friendly
# error message. Test your program by entering two numbers and then by
# entering some text instead of a number
print('10.6 Addition')


def addition():
    print('Simple Addition')
    number1 = input('Please enter a number you want to add: ')
    number2 = input('Please enter your second number: ')
    try:
        answer = int(number1) + int(number2)
    except ValueError:
        print('Error: Please enter only numbers.')
    else:
        print(f'The answer is: {answer}')


addition()
print('\n')


# 2.On page 202 of your book, do 10-7 of the Try it Yourself. Put all your
# code in your exercise12.py file.
print('#2 Problem')
# 10-7. Addition Calculator: Wrap your code from Exercise 10-6 in a while loop
# so the user can continue entering numbers even if they make a mistake and
# enter text instead of a number.
print('10.7 Addition Calculator')


def addition_loop():
    condition = True
    while condition:
        print('\nLoop Addition')
        number1 = input('Please enter a number you want to add: ')
        number2 = input('Please enter your second number: ')
        try:
            answer = int(number1) + int(number2)
        except ValueError:
            print('Error: Please enter only numbers.')
        else:
            print(f'The answer is: {answer}')
            condition = False


addition_loop()
print('\n')


# 3.On page 202 of your book, do 10-8 of the Try it Yourself. Put all your
# code in your exercise12.py file.
print('#3 Problem')
# 10-8. Cats and Dogs: Make two files, cats.txt and dogs.txt. Store at least
# three names of cats in the first file and three names of dogs in the second
# file. Write a program that tries to read these files and print the contents
# of the file to the screen. Wrap your code in a try-except block to catch
# the FileNotFound error, and print a friendly message if a file is missing.
# Move one of the files to a different location on your system, and make sure
# the code in the except block executes properly.
print('10.8 Cats and Dogs')


def file_reader():
    filenames = ['cats.txt', 'dogs.txt']
    try:
        with open(filenames[0]) as f:
            cats = f.read()
        with open(filenames[1]) as f:
            dogs = f.read()
    except FileNotFoundError:
        print('Error, file not found')
    else:
        cat_names = cats.split()
        dog_names = dogs.split()

        for cat in cat_names:
            print(f'Cat is named {cat}')
        for dog in dog_names:
            print(f'Dog is named {dog}')


file_reader()
print('\n')


# 4.On page 202 of your book, do 10-9 of the Try it Yourself. Put all your
# code in your exercise12.py file.
print('#4 Problem')
# 10-9. Silent Cats and Dogs: Modify your except block in Exercise 10-8 to fail
# silently if either file is missing.
print('10.9 Silent Cats and Dogs')


def file_reader_silent():
    filenames = ['cats.txt', 'dogs.txt']
    try:
        with open(filenames[0]) as f:
            cats = f.read()
        with open(filenames[1]) as f:
            dogs = f.read()
    except FileNotFoundError:
        pass
    else:
        cat_names = cats.split()
        dog_names = dogs.split()

        for cat in cat_names:
            print(f'Cat is named {cat}')
        for dog in dog_names:
            print(f'Dog is named {dog}')


file_reader_silent()
