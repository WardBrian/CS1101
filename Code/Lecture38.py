# pylint: disable=c


def square(x):
    return x**2


def is_even(x):
    return x % 2 == 0


given_list = [1, 2, 3, 4]
map_result = map(square, given_list)
print map_result

comprehension_result = [value**2 for value in given_list]
print comprehension_result

map(str, given_list)
str_list = [str(value) for value in given_list]
print str_list

ones = [1 for _ in range(10)]
print ones


# same problem as the former lecture
def square_evens(list_in):
    return map(square, filter(is_even, list_in))


map_filter_result = square_evens(given_list)
print map_filter_result

comprehension_result2 = [value**2 for value in given_list if value % 2 == 0]
print comprehension_result2

nested = [[1, 2, 3], [4, 5], [6], [7, 8, 9]]
flattened = [value for sublist in nested for value in sublist]
print flattened

mtx = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_mtw = [[value * 2 for value in row] for row in mtx]
print new_mtw

comprehension_set = {x for x in range(10)}
print comprehension_set

comprehension_dict = {x: x**2 for x in range(10)}
print comprehension_dict
