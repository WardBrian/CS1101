# pylint: disable=c,w

# list1 = [1, 2, 7, 10, -1]
# derived = [x**2 for x in list1]
# # can also use indecies, first one is MUCH better however
# derived2 = [list1[i]**2 for i in range(len(list1))]
# print derived, derived2
#
# list2 = [(x, x**2) for x in list1]
# print list2

# n = 3
# # [x for x in range(...)] is identical to range(...)
# basic_mtx = [range(1, n + 1) for i in range(n)]
# print basic_mtx
#
# ascending_mtx = [[x + n * j for x in range(1, n + 1)] for j in range(n)]
# print ascending_mtx
#
# mtx = ascending_mtx  # alias it so this is shorter
# column_index = 1
# column = [row[column_index] for row in mtx]
# print column
#
# filename = 'imdb.txt'
# file_object = open(filename, 'r')
# file_list = [line.rstrip() for line in file_object]
# file_object.close()
#
# # another way to do file handling
# # context manager
# with open(filename, 'r') as file_handle:
#     # do whatever
#     file_list = [line.rstrip() for line in file_handle]
# # outside here, the file has been closed
# print file_handle.closed, file_list[:5]

# # filter functionality
# list1 = [1, 2, 3, 4, 5]
# list2 = (map(lambda x: x**2, filter(lambda x: x % 2 == 0, list1)))
# list2
# # same map/filter behavior can be replaced with list comprehension
# list3 = [x**2 for x in list1 if x % 2 == 0]
# list3

list1 = [-1, 1, 3, -4, -5, 10]
list2 = [x**3 for x in list1 if x > 0]
list2

# using 'conditional expressions' you can include else
# this is fundamentally different
list3 = [x**3 if x > 0 else x**2 for x in list1]
list3

# dmx test
# import pysimpledmx
# mydmx = pysimpledmx.DMXConnection(0)
