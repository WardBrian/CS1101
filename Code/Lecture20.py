# pylint: disable=c
# list1 = []
# list1.append(20)
# # No assignment needed
# print list1
# str1 = 'Boston University'
# str1.replace('University', 'College')
# # Does NOT modify str1
# print str1

# list1 = [10, 2, 3, 2, 2, 4, -1]
# list1.remove(2)
# print list1
# list1.insert(2, 100)
# print list1
# list1.pop(2)
# print list1

# month31 = ['JAN', 'MAR', 'MAY', 'JUL', 'AUG', 'OCT', 'DEC']
# month30 = ['APR', 'JUN', 'SEP', 'NOV']
# month28 = ['FEB']
# all_months = month31 + month30 + month28
# user_month = raw_input('Please enter the three letter code for your month: ')
# if user_month in month31:
#     print 'Your month has 31 days'
# elif user_month in month30:
#     print 'Your month has 30 days in it'
# elif user_month in month28:
#     print 'You entered Feburary'
# else:
#     print 'Invalid input'

# first_half = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN']
# second_half = ['JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']
# months = first_half + second_half
#
# length = len(months)
# for index in range(length):
#     print months[index]  # -> an individual month
#
# for month in months:
#     print month

# def upper_all(list_in):
#     list_out = []
#     for element in list_in:
#         list_out.append(element.upper())
#     return list_out
#
#
# upper_all(['Jan', 'feb', 'maR', 'APR'])

# list1 = [10, 232, -5, 45]
# min(list1)
# max(list1)
# sum(list1)
# avg = float(sum(list1)) / len(list1)

# def fibonacci(N):
#     fib = [0, 1]
#     for _ in range(2, N):
#         # [-2:] gets final two values in a sequence
#         next_val = sum(fib[-2:])
#         fib.append(next_val)
#     return fib
#
# fibonacci(20)
