# pylint: disable=w,c
#
# # Errors
#
# # ZeroDivision
# 1 / 0
#
# # IO
# file_object = open('nonexistant.txt', 'r')
#
# # Index
# list1 = [1, 10, 100]
# list1[3]
#
# # Key
# dict1 = {'a': 10, 'c': 100, 'd': 0}
# dict1['b']
#
# # Name
# print y
#
#
# # UnboundLocal
# def fun(x):
#     z = z + 1
#     print z
#     return None
#
#
# fun(10)
#
# # Type
# x = 'a'
# 10 / x
#
# # Value
# import math
# math.sqrt(-4)
#
# # Exception Handling
# try:
#     # Whatever code you suspect may raise an Exception
#     # Either there is an Exception or it works and we move on
#     file_object = open('imdb.txt', 'a')
#     print math.sqrt(-4)
#     # This area here is ONLY executed if it doesn't throw Exceptions
# except IOError:
#     # Do whatever is apropriate in the case of an IOError
#     print 'Your file does not exist'
# except ValueError:
#     # Do something else for ValueError
#     print 'The values you gave me are kinda shaky'
# else:
#     # This is the clean case
#     # Whatever is apropriate when no Exception
#     # result = processor(file_object)
#     print file_object.mode
# finally:
#     # NO MATTER WHAT happens, run this code
#     # THIS WILL EVEN RUN IF THE EARLIER BLOCK RETURNED SOMETHING or had an uncaught Exception
#     file_object.close()
#
# print 'Done with that block'
# print file_object.closed
#
# # Another example
# grade_sum = 900
# while True:
#     try:
#         num = int(raw_input('How many students?'))
#         avg = float(grade_sum) / num
#     except ValueError:
#         print 'The value you gave makes no sense. Is it an integer?'
#     except ZeroDivisionError:
#         print "Are you sure you have no students?"
#     else:
#         print 'The average score was', avg
#         break

import sys


def read_file():
    file_object = open('imdb.txt', 'r')
    master_list = [line.strip() for line in file_object]
    file_object.close()
    return master_list


def make_actor_dict():
    """Create the actor-titles dictionary for Part 2.
    The keys are actors. The value associated with each key (actor) is the
    set of movies that the actor has been in.
    """
    master_list = read_file()
    actor_title = {}
    for j in range(0, len(master_list), 2):
        title = master_list[j]
        actor = master_list[j + 1]
        if actor not in actor_title:
            actor_title[actor] = {title}
        else:
            actor_title[actor].add(title)
    return actor_title


def actor_lookup():
    actor_title = make_actor_dict()
    actor = raw_input('Who do you want to look up?')
    try:
        their_movies = actor_title[actor]
    except KeyError:
        print 'Your actor does not exist in the dictionary'
    else:
        print their_movies
        return None


actor_lookup()
