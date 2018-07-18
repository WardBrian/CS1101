# pylint: disable=c


# Problem 1
def print_odds1(num):
    for number in range(1, num + 1, 2):
        print number


def print_odds2(num):
    number = 1
    while number <= num:
        print number
        number += 2


print_odds1(23)
print_odds2(34)


# Problem 2
# This one is a doozy. First of all, they don't cast raw_input to an int, so all their comparisons are meaningless
# Furthermore, They only update the loop condition if the answer is not 2 or 3,
# values they specifically requested, and they never tell the user what to input to quit.
# Besides UX concerns, generally speaking their loop condition should be something more meaningful
# Allow me to humbly suggest:
def noninfinite_loop():
    test = int(raw_input('Enter the number 2 or 3: '))
    while test != 2 and test != 3:
        print 'Not 2 or 3'
        test = int(raw_input('No! Enter the number 2 or 3: '))
    print 'You entered', test
    return None


noninfinite_loop()


# Problem 3
def print_no_whitespace(word):
    # Use a for loop to directly traverse the string
    for char in word:
        if char != ' ':
            print char


print_no_whitespace('Hello    Worl d')


# Problem 4
def is_vowel(char):
    no_case = char.lower()
    return no_case == 'a' or no_case == 'e' or no_case == 'i' or no_case == 'o' or no_case == 'u'  # or no_case == 'y'


def get_vowels(word):
    vowels = ''
    for char in word:
        if is_vowel(char):
            vowels += char
    return vowels


print get_vowels("Hello Arianna")


# Problem 5
def weird_sum1(num):
    r_sum = 0
    for x in range(num - 10, num + 1):
        r_sum += x
    return r_sum


def weird_sum2(num):
    r_sum = 0
    cur = num - 10
    while cur <= num:
        r_sum += cur
        cur += 1
    return r_sum


weird_sum1(100)
weird_sum2(10)
