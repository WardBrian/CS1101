#pylint: disable=w,c
#
# import math
#
#
# def circle_area(radius):
#     """Calculate the area of a circle with the given radius
#
#     Arguments:
#     radius--the radius of the circle.
#     """
#     return math.pi * radius
#
#
# def print_circle_area(radius):
#     """Print the area of a circle with the given radius
#
#     Arguments:
#     radius--the radius of the circle.
#     """
#     print 'The area is', math.pi * radius
#     return None
#
#
# area1 = circle_area(2)
# print area1
#
# area2 = print_circle_area(2)
# print area2

# def doubleIt(x):
#     return x * 2
#
#
# x = doubleIt(doubleIt(doubleIt(2)))
# print x

import math


def circle_area(radius):
    return radius**2 * math.pi
    # Code here would never get called


def cone_area(height, radius):
    return circle_area(radius) * height / 3.0


radius = 5
height = 2

volume = cone_area(height, radius)
print 'The volume is', volume
