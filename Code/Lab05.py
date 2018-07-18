# pylint: disable=c
# Problem 1
def countdown():
    print 'Begin the countdown!'
    for count in range(10, 0, -1):
        print count
    print 'Finish!'
    return None


countdown()


# Problem 2
def gcd(a, b):
    c = a % b
    while c != 0:
        a = b
        b = c
        c = a % b
    return b


gcd(63, 132)


# Problem 3
def repeat(string, num):
    new_string = ''
    for _ in range(num):
        new_string += string
    return new_string


repeat('hello world', 10)


# Problem 4
def lcm1(num1, num2):
    return num1 * num2 / gcd(num1, num2)


def lcm2(num1, num2):
    for number in range(max(num1, num2), num1 * num2 + 1):
        if (number % num1 == 0) and (number % num2 == 0):
            return number
    return 0


lcm1(2, 5)
lcm2(16, 72)


# Problem 5
def create_list():
    list1 = []
    while True:
        user_input = raw_input('Enter an integer or q to quit: ')
        if user_input.lower() == 'q':
            break
        list1.append(int(user_input))
    return list1


create_list()
