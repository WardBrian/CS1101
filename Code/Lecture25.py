# pylint: disable=c

dict1 = {}
dict1['Sarah'] = 'blue'
dict1['Mark'] = 'black'
# Keys must be unique
dict1['Mark'] = 'red'

dict1['Jace'] = 'blue'

print dict1
#
# dict1.keys()
# dict1.values()
# dict1.items()
# print zip(dict1.keys(), dict1.values()) == dict1.items()
#
# # Can define dicts another way
# dict2 = {'Sarah': 18, 'Jace': 20, 'Mark': 19}
# print dict2
#
#
# def find_key(dictionary, value):
#     """Find a key associated with the given value in the given dict, if it exists"""
#     for key in dictionary:
#         if dictionary[key] == value:
#             return key
#     return None
#
#
# print find_key(dict2, 19)
# print find_key(dict2, 120)

# def create_hist(grade_list):
#     hist = {}
#     for x in range(1, 5):
#         hist['bucket ' + str(x)] = 0
#     for grade in grade_list:
#         if grade >= 90:
#             hist['bucket 1'] += 1
#         elif grade >= 80:
#             hist['bucket 2'] += 1
#         elif grade >= 70:
#             hist['bucket 3'] += 1
#         else:
#             hist['bucket 4'] += 1
#     return hist
#
#
# grade_list1 = [100, 98, 76, 65, 61, 80, 75, 96, 90, 67, 87]
# hist1 = create_hist(grade_list1)
#
# for i in range(1, 5):
#     print 'In bucket', str(i), 'there are', hist1['bucket ' + str(i)], 'grades'

set1 = {'BC', 'BU', 'NEU', 'HVD', 'BC', 'BC'}
print set1

print {1, 2, 2, 3, 3} == {1, 2, 3} == {3, 2, 1}

{1, 3, 4, 5, 2}.intersection({4, 5, 7})
