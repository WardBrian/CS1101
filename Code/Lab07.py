# pylint: disable=c

import capitals, random


# Problem 1
def set_item(input_tuple, index, new_value):
    if index < 0 or index >= len(input_tuple):
        return input_tuple
    list1 = list(input_tuple)
    list1[index] = new_value
    return tuple(list1)


set_item((1, 10, 100, 30), 2, -20)


# Problem 2
def create_dict(keys, values):
    return dict(zip(keys, values))


def create_dict2(keys, values):  # How you probably wanted it
    dict1 = {}
    for i in range(len(keys)):
        dict1[keys[i]] = values[i]
    return dict1


create_dict(['a', 'b', 'c', 'd'], [1, 2, 3, 4])
create_dict2(['a', 'b', 'c', 'd'], [1, 2, 3, 4])


#Problem 3
def dictionaried_primes(list_in):
    dict1 = {'primes': [], 'twos': [], 'threes': []}
    for number in list_in:
        if is_prime(number):
            dict1['primes'].append(number)
        if number % 3 == 0:
            dict1['threes'].append(number)
        if number % 2 == 0:
            dict1['twos'].append(number)

    return dict1


# Problem 4
def game():
    capitals_dict = capitals.capitals_dict
    key_list = capitals_dict.keys()
    while True:
        state = random.choice(key_list)
        user_input = raw_input('Guess the capital of ' + state +
                               ' or enter Q to quit')
        if user_input.lower() == 'q':
            break
        if user_input == capitals_dict[state]:
            print 'You got it right!'
        else:
            print 'Wrong. The answer was', capitals_dict[state], ':('

    print 'Thanks for playing'
    return None


game()
