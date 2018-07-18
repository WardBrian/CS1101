# pylint: disable=c

# def candy_distribution(candypieces, people):
#     try:
#         return candypieces / people, candypieces % people
#     except ZeroDivisionError:
#         print "The number of people cannot be zero!"
#         return None
#     finally:
#         if candypieces < 100:
#             print 'Try harder next time'
#
#
# result = candy_distribution(98, 7)
# try:
#     num1, num2 = result
# except:
#     pass
# else:
#     print 'Everyone gets', num1, 'candies'
#     print 'There are', num2, 'candies left over'

# like raw_input, but does casting for you. Not in python3, usually not used
# can directly enter tuples, lists, etc
# returned_value = input('give me an input please: ')
# print type(returned_value), returned_value

# import math
#
# def quadratic_solver():
#     try:
#         tuple_in = input('Please enter (a,b,c)')
#         a, b, c = tuple_in
#         disc = b**2 - 4 * a * c
#         sol1 = (-b + math.sqrt(disc)) / (2 * a)
#         sol2 = (-b - math.sqrt(disc)) / (2 * a)
#     except TypeError:
#         print 'You need to enter numbers!'
#         # return quadratic_solver() # a recursive call here would loop it
#     except ValueError:
#         print 'Your numbers have no real solutions'
#     # the 'as' keyword will store the message in any valid name
#     except ZeroDivisionError as msg:
#         print 'Please do not enter 0 for a, that is not a quadratic'
#         print msg
#     else:
#         return sol1, sol2
#
#
# quadratic_solver()
#
#
# def add(a, b):
#     return a + b
#
#
# def subtract(a, b):
#     return a - b
#
#
# def multiply(a, b):
#     return a * b
#
#
# g = add
# g(2, 4)
# print add
# fun_list = [add, subtract, multiply]
# print fun_list
# fun_list[2](2, 7)  # synonymous with multiply(2,7)

import math


def square(x):
    return x**2


def double(x):
    return 2 * x


def half(x):
    return x / 2.0


def mapfunc(func, alist):
    """A map function"""
    new_list = []
    for value in alist:
        new_list.append(func(value))
    return new_list


list1 = [1, 2, 3, 4]
mapfunc(square, list1)
mapfunc(math.sqrt, list1)

list_words = 'Hello how are you?'.split()
map(len, list_words)

map(square, list1)
map(math.sqrt, list1)
map(half, list1)


def is_even(x):
    return x % 2 == 0


def filterfun(func, alist):
    result = []
    for value in alist:
        if func(value):
            result.append(value)
    return result


list2 = [1, 2, 3, 4, 5, 6, 0]
filterfun(is_even, list2)
filter(is_even, list2)
# oh shit lambdas exist in python
filter(lambda x: x % 3 == 0, list2)


def square_evens(list_in):
    return map(square, filter(is_even, list_in))


list4 = [1, 2, 0, -2, 3, 4]
print square_evens(list4)


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def reducefun(func, alist):
    final = alist[0]
    for value in alist[1:]:
        final = func(final, value)
    return final


list3 = [1, 2, 3, 4, 5]
reducefun(add, list3)
reducefun(lambda x, y: x + y, list3)
reduce(lambda x, y: x + y, list3)
reduce(add, list3)
reduce(multiply, list3)
reduce(lambda x, y: x * y, list3)
