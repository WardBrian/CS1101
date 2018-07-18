# pylint: disable=c

# [1, 2, 3, 4]
#
# type([1, 2])
# [1, 2] == [2, 1]

# list1 = [1, 2, -10, 50, 20, 30, -21]
# print list1[0]
# print list1[-1]
# print list1[:4]
# print list1[::-1]

# cheeses = ['Mozzerella', 'Parmesan', 'Cheddar', 'American']
# veggies = ['Broccoli', 'Spinach']
# meats = ['Pepperoni', 'Proscuitto', 'Bacon']
#
# toppings = cheeses + veggies + meats
# print 'The toppings are', toppings
#
# count = 0
# while True:
#     topping = raw_input('Enter your topping, or Q to quit: ')
#     if topping.lower() == 'q':
#         break
#     count += 1
#
# if count <= 3:
#     price = 9.99
# else:
#     price = 9.99 + (count - 3) * 1.25
#
# print 'Your pizza cost $' + str(price)

# cheese = ['Mozzerella', 'Parmesan', 'Cheddar', 'American']
# cheese[1] = 'Sharp Cheddar'
# print cheese
# cheese[:2] = ['Swiss', 'Baby Swiss']
# print cheese
# cheese[:2] = []
# print cheese

# list1 = list()
# print list1
list1 = []
print list1
x = 2
# append x to list1
# Could use +, but is better to use methods
list1.append(x)
print list1
