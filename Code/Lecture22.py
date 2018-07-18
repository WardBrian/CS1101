# pylint: disable=c

# ALIASING OF IMMUTABLE OBJECTS
first = 1000
second = first
print first, second
first += 3
print first, second

first = 'Boston'
second = first
print first, second
first += ' College'
print first, second

# ALIASING OF MUTABLE OBJECTS
first = [1, 2]
second = first
print first, second
first.append(3)  # append is in place
print first, second

# using [:] will generate a copy of a sequence
first = [1, 2]
second = first[:]
print first, second
first.append(3)
print first, second

# assignment is NOT in place
first = [1, 2]
second = first
print first, second
first = [3]
print first, second

# BAD
list1 = [1, 2, 2, 3, 4, 5]
list2 = [2, 3]
for element in list1:
    if element in list2:
        list1.remove(element)
print list1

# GOOD
list1 = [1, 2, 2, 3, 4, 5]
list2 = [2, 3]
for element in list1[:]:
    if element in list2:
        list1.remove(element)
print list1
