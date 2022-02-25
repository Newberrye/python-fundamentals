# 1.Write a function called simple(). Assign a different message to 5
# variables and print each message.
def simple():
    message1 = "I wanna be the very best"
    message2 = "Like no one ever was"
    message3 = "To catch is my real test"
    message4 = "To train them is my cause"
    message5 = "I will travel across the land"

    print("#1 Simple Function")
    print(message1); print(message2); print(message3); print(message4)
    print(message5)
    print()


simple()


# 2.Write a function called simple2(). Assign a message to a variable,
# then print out that variable. Change the message and assign it to the
# variable again, but after the first print statement. Print the second
# message. Do these steps 2 more times. You should have 4 messages assigned
# to the same variable and 4 print functions showing the results.
def simple2():
    print("#2 Simple2 Function")
    message = "Searching far and wide"
    print(message)

    message = "These Pokemon to understand the power  that's inside"
    print(message)

    message = "Pokemon gotto catch them all"
    print(message)

    message = "It's you and me"
    print(message)
    print()


simple2()


# 3.Write a function called message that takes 1 argument. Inside that
# function, write a print function that takes the argument.
def message(message):
    print("#3 Message Function with a Parameter")
    print(message)


message("I know it's my destiny")
