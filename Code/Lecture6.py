# pylint: disable=w,c

# def starry_box(phrase):
#     """This function takes a str and prints it in a box made of asterix"""
#     top_line = '*' * (len(phrase) + 4)
#     print top_line
#     print '*', phrase, '*'
#     print top_line
#     return
#
#
# starry_box(raw_input('What should be printed in the starry box?'))
from math import pi


def print_cone_volume(height, radius):
    """Print the volume of the cone with a given height and radius.

    Arguments:
    height--The height of the cone
    radius--The radius of the base of the cone
    """
    volume = pi / 3 * height * radius**2
    print 'The volume of the cone is', volume
    return


def cone_volume(height, radius):
    """Calculate the volume of the cone with a given height and radius.

    Arguments:
    height--The height of the cone
    radius--The radius of the base of the cone
    """
    volume = pi / 3 * height * radius**2
    return volume


print_cone_volume(5, 2)
print_cone_volume(2, 5)
volume = cone_volume(5, 2)
print volume
