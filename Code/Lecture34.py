# pylint: disable=c

# count = 0
# file_handle = open('imdb.txt', 'r')
# for line in file_handle:
#     # line becomes each line
#     # print line.rstrip()
#     count += 1
# # close your file
# file_handle.close()
#
# print count
#
# '\n'


# get the user's movie, return the size of the cast for that film
def get_cast_size(movie_name):
    cast_size = 0
    file_handle = open('imdb.txt', 'r')
    for line in file_handle:
        if line.rstrip() == movie_name:
            cast_size += 1
    file_handle.close()
    return cast_size


movie = raw_input('Please enter a movie')
size = get_cast_size(movie)
print 'There are', size, 'actors in', movie + '.'

file_object = open('test.txt', 'a')
string = 'Computer Science II'
file_object.write(string + '\n')
file_object.close()

str_list = [
    'Computer Science',
    'Computer Science 2',
    'Algorithms',
    'More classes',
]

file_object = open('test.txt', 'w')
for string in str_list:
    file_object.write(string + '\n')
file_object.close()
