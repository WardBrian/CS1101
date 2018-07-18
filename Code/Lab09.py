# pylint: disable=c


def create_character_dictionary(filename):
    char_dict = {}
    try:
        file_object = open(filename, 'r')
    except IOError:
        # return an empty dictionary
        return char_dict
    else:
        for line in file_object:
            for char in line.rstrip():
                try:
                    char_dict[char] += 1
                except KeyError:
                    char_dict[char] = 1
        file_object.close()
        return char_dict


def save_dictionary(dict1, filename):
    file_object = open(filename, 'w')
    for key in dict1:
        str_line = str(key) + ':' + str(dict1[key]) + '\n'
        file_object.write(str_line)
    file_object.close()
    return None


character_dict = create_character_dictionary('sonnets.txt')
save_dictionary(character_dict, 'CharacterCount.txt')
