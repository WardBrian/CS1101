# pylint: disable=c

big_tuple = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9), )

print big_tuple
second_row = big_tuple[1]
print second_row

# change (4,5,6) to (4,2,6)
second_row = second_row[:1] + (2, ) + second_row[2:]
print second_row

# Now insert that into big_tuple
big_tuple = big_tuple[:1] + (second_row, ) + big_tuple[2:]
print big_tuple

#
#
#
#
#
#
#
#
#

# open the file in 'read' mode
file_object = open('imdb.txt', 'r')

print file_object

# Always close the file when you are done
file_object.close()
print file_object.closed  # True here
print file_object.name
print file_object.mode

file_object = open('imdb.txt', 'r')

count = 0
for line in file_object:
    if count == 0:
        print line
        first_line = line
        count += 1
print first_line

string = '\n'
print len(string)

print 'hi\nbye'

print first_line
stripped = first_line.rstrip()
print stripped
