# pylint: disable=c


def fib(number):
    if number == 0 or number == 1:
        return number
    return fib(number - 1) + fib(number - 2)


fib(6)


def fib_smarter(n):
    dict1 = {0: 1, 1: 1}
    return fib_helper(n, dict1)


def fib_helper(n, dict1):
    if n in dict1:
        return dict1[n]
    val = fib_helper(n - 1, dict1) + fib_helper(n - 2, dict1)
    dict1[n] = val
    return val


fib_smarter(40)


def linear_search_unordered(list1, val):
    """Determine whether the given value exists in the given list"""
    for current_value in list1:
        if current_value == val:
            return True
    return False


def rec_linear_search(list1, val):
    """Recursively determine whether the given value exists in the given list"""
    if not list1:
        return False
    if list1[0] == val:
        return True
    return rec_linear_search(list1[1:], val)


def linear_search(sorted_list, val):
    """Determine whether the given value exists in the given SORTED list

    Assumption: sorted_list is sorted in ascending order
    """
    if not sorted_list:  # If list is empty it evaluates to false
        return False
    if val < sorted_list[0] or val > sorted_list[-1]:  # If not between greatest and least
        return False
    for current_value in sorted_list:
        if current_value == val:
            return True
        if current_value > val:  # Because list is ascending
            return False
    return False


def binary_search(sorted_list, val):
    """Determine whether the given value exists in the given SORTED list

    Assumption: sorted_list is sorted in ascending order
    """
    if not sorted_list:  # If list is empty it evaluates to false
        return False
    if val < sorted_list[0] or val > sorted_list[-1]:  # If not between greatest and least
        return False
    # find the value sitting in the middle of the list
    low = 0
    high = len(sorted_list) - 1
    while low <= high:
        mid = (high + low) / 2
        mid_val = sorted_list[mid]
        if mid_val == val:
            return True
        if mid_val > val:
            high = mid - 1
        else:
            low = mid + 1
    return False


def rec_binary_search(sorted_list, val):
    """Recursively determine whether the given value exists in the given SORTED list

    Assumption: sorted_list is sorted in ascending order
    """
    if not sorted_list:  # If list is empty it evaluates to false
        return False
    if val < sorted_list[0] or val > sorted_list[-1]:  # If not between greatest and least
        return False
    return rec_binary_search_helper(sorted_list, val, len(sorted_list) - 1, 0)


def rec_binary_search_helper(sorted_list, val, high, low):
    """The actual recursive method, called from the wrapper rec_binary_search"""
    if low > high:
        return False
    mid = (high + low) / 2
    mid_val = sorted_list[mid]
    if mid_val == val:
        return True
    if mid_val > val:
        return rec_binary_search_helper(sorted_list, val, mid - 1, low)
    return rec_binary_search_helper(sorted_list, val, high, mid + 1)


my_list = [-1, 2, -10, 7, 1, 3, -6]
my_list.sort()
print my_list
print linear_search_unordered(my_list, 3)
print linear_search_unordered(my_list, 30)
print rec_linear_search(my_list, 3)
print rec_linear_search(my_list, 30)
print linear_search(my_list, 3)
print linear_search(my_list, 30)
print binary_search(my_list, 3)
print binary_search(my_list, 30)
print rec_binary_search(my_list, 3)
