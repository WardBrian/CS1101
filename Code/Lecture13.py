# pylint: disable=c

# number = 1
# while number < 10:
#     print number
#     number += 1
# print 'We are outside the while loop'
s = 'Hello World'

i = 0
while i < len(s):
    print s[i]
    i += 1
#probably better to do
for i in range(len(s)):
    print s[i]
