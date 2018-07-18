# pylint: disable=c

# def count_char(string, to_find):
#     count = 0
#     for char in string:
#         if char == to_find:
#             count += 1
#     return count
#
#
# def more_As(string1, string2):
#     if string1.count('A') >= string2.count('A'):
#         return string1
#     return string2
#
#
# more_As('BANANAAA', 'bAnAnaaaaaaaaaaaaaaa')

# def test_palindrome(string):
#     string = string.lower()
#     return string == string[::-1]

# This one checks individual characters
# def test_palindrome(string):
#     string = string.lower()
#     n = len(string)
#     for index in range(n / 2):
#         if string[index] != string[-index - 1]:
#             return False
#     return True
#
#
# test_palindrome('Racecar')
# test_palindrome('abba')
# test_palindrome('Motorcycle')


def print_fib(number):
    """number has to be >=2, and an integer"""
    num0 = 0
    num1 = 1
    print num0, num1,
    for _ in range(number - 2):
        num2 = num0 + num1
        print num2,
        num0 = num1
        num1 = num2
    return None


print_fib(1000)

import math


def is_prime(n):
    if n == 2:
        return True
    for x in range(2, int(math.sqrt(n)) + 1):
        if n % x == 0:
            return False
    return True


is_prime(223)
