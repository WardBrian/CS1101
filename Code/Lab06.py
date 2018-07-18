# pylint: disable=c


# Problem 1
def even(number):
    if number < 0:
        number = -number
    even_list = []
    for integer in range(number, 2 * number + 1):
        if integer % 2 == 0:
            even_list.append(integer)
    return even_list


print even(-7)


# Problem 2
def problem_two(number, int1):
    list1 = even(number)
    list2 = []
    for element in list1:
        if element % int1 != 0:
            list2.append(element)
    return list2


print problem_two(7, 3)


# Problem 3
def rearrange(list1):
    list2 = []
    for index in range(len(list1)):
        if index % 2 == 0:
            list2.append(list1[index])
        else:
            list2.insert(0, list1[index])
    return list2


print rearrange([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])


# Problem 4
def longest_string(list1):
    max_index = 0
    for index in range(len(list1)):
        if len(list1[index]) > len(list1[max_index]):
            max_index = index
    return list1[max_index]


# I like this one much better, but I already did the first one so I'm keeping it
def longest_string2(list1):
    string = ''
    for element in list1:
        if len(element) > len(string):
            string = element
    return string


print longest_string(['Strongest', 'Strong', 'Stronger', 'Strongeriest'])
print longest_string2(['Strongest', 'Strong', 'Stronger', 'Strongeriest'])
