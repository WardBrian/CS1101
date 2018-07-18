# pylint: disable=c
def rec_multiplication(real_num, nonnegative_int):
    """ Use recursion to compute real_num * nonegative_int

    Arguments:
    real_num--Any float
    nonnegative_int--Any non-negative integer
    """
    if nonnegative_int == 0:
        return 0
    return real_num + rec_multiplication(real_num, nonnegative_int - 1)


rec_multiplication(2.2, 7)


def reverse_str(string):
    """Reverse the given string using a recursive algorithm

    Arguments:
    string-- any valid Python string"""
    if string == '':
        return string
    return string[-1] + reverse_str(string[:-1])


reverse_str('Hello world')


def is_palindrome(string):
    if string == '':
        return True
    return (string[0] == string[-1]) and is_palindrome(string[1:-1])


is_palindrome('aba')
