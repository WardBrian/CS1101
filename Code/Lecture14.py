# pylint: disable=c
#
# strin = 'Hello World'
#
# index = 0
# length = len(strin)
#
# while index < length:
#     print strin[index]
#     index += 1
#
# for index in range(length):
#     print strin[index]
#
# for char in strin:
#     print char

import random

while True:
    question = raw_input(
        "Hey, ask me anything you want (or enter 'q' to quit):")

    if question.lower() == 'q':
        break

    answer = random.randint(1, 4)  # random number between 1-4, inclusive
    if answer == 1:
        msg = 'Signs point to yes'
    elif answer == 2:
        msg = 'My sources say no!'
    elif answer == 3:
        msg = "I'm not sure"
    else:
        msg = "Definitely, go for it"
    print msg

print 'Thanks for playing!'
