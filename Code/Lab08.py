# pylint: disable = c


# Problem 1
def period_count(string):
    if string == '':
        return 0
    if string[0] == '.':
        return 1 + period_count(string[1:])
    return period_count(string[1:])


period_count('a...b..a.')


# Problem 2
def print_triangle(number):
    print '*' * number
    if number != 1:
        print_triangle(number - 1)
    return None


print_triangle(6)


# Problem 3
def rec_gcd(num1, num2):
    num3 = num1 % num2
    if num3 == 0:
        return num2
    return rec_gcd(num2, num3)


rec_gcd(58, 124)


# Problem 4
# This is a pow function. It returns first ** second
def mystery(first, second):
    if second == 0:
        return 1
    if second % 2 == 0:
        return mystery(first * first, second / 2)
    return first * mystery(first * first, second / 2)


# b it then becomes a multiplcation function

mystery(2, 5)


def mystery2(first, second):
    if second == 0:
        return 0
    if second % 2 == 0:
        return mystery2(first + first, second / 2)
    return first + mystery2(first + first, second / 2)


mystery2(6, 6)


# Problem 5
def create_list():
    user_in = raw_input('Input an integer, or q to quit')
    if user_in.lower() == 'q':
        return []
    return [int(user_in)] + create_list()


create_list()
