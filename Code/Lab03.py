# pylint: disable=c


# Problem 1
def weather_temp(temperature):
    if temperature > 105 or temperature < 20:
        print "Don't go outside!"
    else:
        print 'All clear to go out.'


weather_temp(10)
weather_temp(55)
weather_temp(200)


# Problem 2
def add_repeats(num1, num2):
    if num1 == num2:
        return num1 + num2
    return 0


add_repeats(2, 2)
add_repeats(5, 7)


# Problem 3
def is_positive(num):
    if num > 0:
        return 'Number is positive'
    if num < 0:
        return 'Number is negative'
    return 'Number is 0'


is_positive(-2)
is_positive(0)
is_positive(22)


# Problem 4
def print_name(name):
    for _ in range(5):
        print name


print_name('Brian')


# Problem 5
# this is not the best method to check primality i am certain, but it is fine for small numbers
def check_prime(num):
    for x in range(2, num):
        if num % x == 0:
            return False
    return True


def print_primes():
    for x in range(2, 9):
        if (check_prime(x)):
            print x


print_primes()


# Problem 6
def check_age(age):
    if age < 5 or age >= 75:
        return 'Free!'
    if age < 18:
        return '$10'
    if age < 50:
        return '$15'
    return '$12'


check_age(50)


#Problem 7
def grader(test1, test2, test3):
    sumTest = False
    averageTest = False
    if (test1 < (test2 + test3) / 2.0):
        sumTest = True
    if ((test1 + test2 + test3) / 3.0) >= 90:
        averageTest = True

    if (averageTest and sumTest):
        return 'A+'
    if (averageTest != sumTest):
        return 'A'
    return 'C'


grader(91, 93, 94)
grader(100, 80, 92)
grader(91, 91, 90)
grader(100, 70, 70)
