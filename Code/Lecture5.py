# # pylint: disable=w,c
# user_input = raw_input('Hello, what is your name? ')
#
# print 'Hi', user_input
#
# user_weight = float(raw_input('What is your weight in pounds? '))
# weight_on_moon = user_weight / 6
# print 'On the moon you will weigh', weight_on_moon, 'lbs'

# #This is not recommended, but does allow you to not use math.
# from math import *
# pi
# sin(0)

# import math
#
# #I want to use the sine function
# math.sin(math.pi)
#
# #Comparing floats often leads to weird results
# .1 + .1 + .1 == .3
# round(.1 + .1 + .1, 2) == .3


def starry_box(phrase):
    """This function takes a str and prints it in a box made of asterix"""
    numStars = len(phrase) + 4
    print '*' * numStars
    print '*', phrase, '*'
    print '*' * numStars
    return


starry_box('Computer Science')
starry_box('BC')
starry_box('Boston College')
