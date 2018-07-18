# # pylint: disable=c
#
# name = 'NEU'
# if name == 'BC':
#     # BC
#     print 'The name is BC.'
# elif name == 'BU':
#     # BU
#     print 'I can have other statements here as well'
# elif name == 'NEU':
#     # NEU
#     print 'They go to Northeastern'
# else:
#     #Harvard
#     print 'Harvard!'
#
# # outside the if statement
#  print 'Out!'

# number = 1
# if number < 2:
#     print 'the number is less than two'
# else:
#     print 'the number is larger than or equal to two'

# import random
# question = raw_input('Hey, ask me anything you want (or press enter to quit):')
# answer = random.randint(1, 4)  # random number between 1-4, inclusive
#
# if question == '':
#     msg = 'Thanks for playing'
# elif answer == 1:
#     msg = 'Signs point to yes'
# elif answer == 2:
#     msg = 'My sources say no!'
# elif answer == 3:
#     msg = "I'm not sure"
# else:
#     msg = "Definitely, go for it"
#
# print msg

month = int(raw_input('Give me the month (as a number):'))
day = int(raw_input('Give me the day (as a number):'))

if month == 1 and day == 1:
    msg = 'Happy New Year!'
elif month == 12 and day == 25:
    msg = 'Merry Christmas!'
elif month == 8 and day == 28:
    msg = 'On no, class!'
else:
    msg = 'Boring'

print msg
