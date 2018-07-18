# pylint: disable=w,c

# Problem 1
words = 'TheQuickBrownFox'
print words[0:3], words[3:8], words[8:13], words[13:16]

# Problem 2
x = 40
y = 1 / 5
print x / 5
print x * y
# Not the same because (1/5) evaluates to 0 in integer division

# Problem 3
name = raw_input('What is your name?')
length = len(name)
print name + ", your name has", length, 'letters'


# Problem 4
def birth_year(age):
    return 2017 - age


input_age = int(raw_input('How old are you?'))
print 'You were born in', birth_year(input_age)


# Problem 5
def average(one, two, three):
    return float(one + two + three) / 3


print average(20, 20, 21), average(1, 2, 3)


# Problem 6
def leap_year(current_year):
    return current_year + (4 - (current_year % 4))


print leap_year(1999), leap_year(2014), leap_year(2016)

# Problem 7
import math


def hypotenuse(a, b):
    return math.sqrt(a**2 + b**2)


print hypotenuse(3, 4)


# Problem 8
def get_age():
    age = int(raw_input('How old are you?'))
    return age


age = 100
returned_age = get_age()
print age
# The original value of age (100) is still printed, because age inside get_age()
# is inside a different frame than age defined in __main__
