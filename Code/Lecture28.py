# pylint: disable=c
def list_product(list1):
    """Recursively compute the product of all the numbers in the given list

    Arguments:
    list1--a non-empty list of integers"""
    if len(list1) == 1:
        return list1[0]
    return list1[0] * list_product(list1[1:])


def list_min(list1):
    """Recursively find min in list1

    Arguments:
    list1--non empty list of numbers"""
    if len(list1) == 1:
        return list1[0]
    remaining_min = list_min(list1[1:])
    if list1[0] > remaining_min:
        return remaining_min
    return list1[0]


def flatten(matrix):
    """Take in nested list and flatten it recursively

    Arguments:
    matrix--non-empty nested list with a depth of 2
    """
    if len(matrix) == 1:
        return matrix[0]

    return matrix[0] + flatten(matrix[1:])


def rotate_right(list1, number):
    """Rotate the list by a given number of elements

    Arguments:
    list1--any valid list1
    number--the number of times to rotate the list
    """
    if number == 0 or len(list1) <= 1:
        return list1
    last_element = list1.pop()
    list1.insert(0, last_element)
    return rotate_right(list1, number - 1)


print rotate_right([1, 2, 3, 4, 5], 2)

candidates = [
    [1, 2, 3],
    [2, 3, 4],
    [-1, 1, 2],
]

for ind_list in candidates:
    print list_product(ind_list)

for ind_list in candidates:
    print list_min(ind_list)

print flatten(candidates)
