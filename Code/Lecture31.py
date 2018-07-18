# pylint: disable=c


def merge(list1, list2):
    """Merge the two given SORTED lists into a list that is also sorted
    Both lists are in increasing order
    """
    merged = []
    index1, index2 = 0, 0
    length1, length2 = len(list1), len(list2)
    while index1 < length1 and index2 < length2:
        if list1[index1] < list2[index2]:
            merged.append(list1[index1])
            index1 += 1
        else:
            merged.append(list2[index2])
            index2 += 1
    # If one reached the end before the other, we need to add the rest
    # One of these will do nothing
    merged.extend(list1[index1:])
    # += is identical to .extend for lists -- in place
    merged += list2[index2:]
    return merged


def merge_sort(list1):
    if len(list1) <= 1:
        return list1
    length = len(list1)
    first_half = list1[:length / 2]
    second_half = list1[length / 2:]
    sorted_first = merge_sort(first_half)
    sorted_second = merge_sort(second_half)
    return merge(sorted_first, sorted_second)


print merge([3, 10, 23, 54], [1, 5, 25, 75])
print merge_sort([6, 203, 7, 2, 0, 0, 9, -1, 22])
