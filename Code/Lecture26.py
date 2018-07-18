# pylint: disable=c

# def algebraic_sum(number):
#     """ Determine the sum of all nonnegative integers between 0 and number
#
#     Arguments:
#     number--An integer >= 0
#     """
#     return int((number + 1.0) / 2.0 * number)
#
#
# algebraic_sum(5000000)
#
#
# def iterative_sum(number):
#     """ Determine the sum of all nonnegative integers between 0 and number
#
#     Arguments:
#     number--An integer >= 0
#     """
#     return sum(range(number + 1))
#
#
# iterative_sum(5000000)


def recursive_sum(number):
    """ Determine the sum of all nonnegative integers between 0 and number

    Arguments:
    number--An integer >= 0
    """
    # base case
    if number == 0:
        return 0
    # recursive case
    return recursive_sum(number - 1) + number


recursive_sum(253)


def recursive_factorial(number):
    """Determine the factorial of the given integer

    Arguments:
    number--A positive integer >= 1
    """
    # base case
    if number == 1:
        return 1
    # recursive case
    return recursive_factorial(number - 1) * number


recursive_factorial(6)
