# pylint: disable=c


def selection_sort(in_list):
    """Sort the given list (in-place) using the selection sort algo"""
    length = len(in_list)
    for index in range(length - 1):
        #find min starting at this index
        minimum, min_index = find_min(in_list, index)
        # swap that min with the value at index
        in_list[min_index] = in_list[index]
        in_list[index] = minimum
    return None


def find_min(in_list, start_ind):
    """Find the minimum starting with index being start_ind through the end
    Returns a tuple of (min, min_index)
    """
    running_min = in_list[start_ind]
    running_min_ind = start_ind
    length = len(in_list)
    for index in range(start_ind, length):
        if in_list[index] < running_min:
            running_min = in_list[index]
            running_min_ind = index
    return running_min, running_min_ind


def insertion_sort(in_list):
    """Sort the given list (in-place) using the selection sort algo"""
    length = len(in_list)
    for i in range(0, length - 1):
        j = i + 1
        next_value = in_list[j]
        # Determine where to insert this next_value into the sorted portion of the list
        while j >= 1 and next_value < in_list[j - 1]:
            # Push the value at j -1 to the right and decrease j
            in_list[j] = in_list[j - 1]
            j -= 1
        # When the while loop is done, insert next_value here
        # the value in_list[j] had just been copied to in_list[j+1]
        in_list[j] = next_value
    return None


list1 = [7, 8, 3, 2, 4, 1, 0, -100]

print list1
#selection_sort(list1)
insertion_sort(list1)
print list1
