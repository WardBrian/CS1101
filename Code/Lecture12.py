#pylint: disable=c

# def my_sum(end):
#     running_sum = 0
#     for x in xrange(end + 1):
#         running_sum = running_sum + x
#     return running_sum
#
#
# def my_even_sum(end):
#     running_sum = 0
#     for x in xrange(2, end + 1, 2):
#         running_sum = running_sum + x
#     return running_sum
#
#
# def actually_good_sum(end):
#     return (end + 1) * (end / 2.0)
#
#
# my_sum(10)
# my_even_sum(10**6)

# def fact(n):
#     r_product = 1
#     for x in xrange(2, n + 1):
#         r_product = r_product * x
#     return r_product
#
#
# fact(2)
# fact(5)


def print_evens(n):
    for x in range(2, n + 1, 2):
        print x


print_evens(1000)
