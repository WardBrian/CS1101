# pylint: disable=c

# str1 = 'Computer Science'
# str2 = 'Computer'
# print str2 in str1
# print not (str2 in str1)
# # Better to use:
# print str2 not in str1


def find_char(string, to_find):
    for index in range(len(string)):
        if string[index] == to_find:
            return index
    return -1


print find_char('Hello', 'e'), 'Hello'.find('e')
