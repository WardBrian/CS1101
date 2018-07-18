# pylint: disable=c
#
# import random
#
# choice = random.randint(0, 100)
# guess = int(raw_input("Make a guess as to which number I've chosen: "))
# while guess != choice:
#     if guess < choice and guess >= 0:
#         print 'Too low, go higher'
#     elif choice < guess and guess <= 100:
#         print 'Too high! Try a lower number!'
#     else:
#         print 'Enter a number in the range, silly!'
#     guess = int(raw_input("Make a guess as to which number I've chosen: "))
#
# print 'You got it!'

# passwrd = ''
# while len(passwrd) != 4:
#     passwrd = raw_input(
#         "Enter a password with exactly four characters, please: ")
# print 'Thanks!'
#
# while True:
#     passwrd = raw_input(
#         "Enter a password with exactly four characters, please: ")
#     if len(passwrd) == 4:
#         break
# print 'Thanks!'


def reverse_str(string):
    new_string = ''
    for char in string:
        new_string = char + new_string
    return new_string


reverse_str('Hello World')

s = 'Hello World'
print s
print s[::-1]
print s[::-1][::-1]

x = 'lo' in 'Hello'
