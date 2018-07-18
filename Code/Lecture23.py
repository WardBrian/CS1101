# pylint: disable=c

empty_list = []
empty_list = list()

empty_tuple = ()
empty_tuple = tuple()

tuple1 = (1, )
tuple2 = 2, 3
tuple3 = tuple1 + tuple2
print tuple3
tuple1 = tuple1 * 10
print tuple1
print tuple1[2:]

# Tuple packing
tuple1 = (1, 2)
tuple1 = 1, 2
# Tuple unpacking
x, y = tuple1
print x
print y


def consolodate_freq(tuple_list):
    word_list = []
    word_count = []
    for string, frequency in tuple_list:
        if string in word_list:
            word_count[word_list.index(string)] += frequency
        else:
            word_list.append(string)
            word_count.append(frequency)
    return zip(word_list, word_count)


consolodate_freq([('BC', 5), ('BU', 4), ('BC', 10), ('NEU', 3), ('BU', 2)])


# Tuple argument collection
def printall(*args):
    for element in args:
        print element


# Replacing just a single character. Make the last 'a' into a 'b'
string1 = 'aaaaaaaaaaaacccccccccccbbaa'

# you could use slicing, but it is extremely slow
print string1[:len(string1) - 1] + 'b'

list_str = list(string1)
list_str[-1] = 'b'
print ''.join(list_str)
