# 1. Hello World
# 1.1 Can you make a typo that generates an error?
# pri nt('Hello World')
#   File "exercise1.py", line 1
#     pri nt('Hello World')
#         ^
# SyntaxError: invalid syntax

# 1.2 Can you make sense of the error message?
# 'nt' is not a base function so there is no syntax for it

# 1.3 Can you make a typo that doesn’t generate an error?
# print("Helo World")
# Helo World

# 1.4 Why do you think it didn't make an error?
# print is a valid function and PyCharm doesn't seem to have a base
# spellcheck for the string inside of print.


# 2. Zen of Python
# import this
# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
# Flat is better than nested.
# Sparse is better than dense.
# Readability counts.
# Special cases aren't special enough to break the rules.
# Although practicality beats purity.
# Errors should never pass silently.
# Unless explicitly silenced.
# In the face of ambiguity, refuse the temptation to guess.
# There should be one-- and preferably only one --obvious way to do it.
# Although that way may not be obvious at first unless you're Dutch.
# Now is better than never.
# Although never is often better than *right* now.
# If the implementation is hard to explain, it's a bad idea.
# If the implementation is easy to explain, it may be a good idea.
# Namespaces are one honking great idea -- let's do more of those!


# 3. Simple Message
# 2.1
print("#3 Simple Message - 2.1")
message = "Hello there General Kenobi."
print(message)
print()

# 2.2
print("#3 Simple Message - 2.2")
message = "You underestimate my power"
print(message)
message = "Fails"
print(message)
print()


# 4.
# 8.1 Message
def display_message():
    print("#4 Functions - 8.1")
    message = "This is how you make a simple function and call it"
    print(message)
    print()


display_message()


# 8.2
def favourite_book(book):
    print("#4 Functions - 8.2")
    message = "One of my favourite books is"
    print(f"{message} {book}.")
    print()


favourite_book("Dune")
