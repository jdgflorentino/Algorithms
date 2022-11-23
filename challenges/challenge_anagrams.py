def is_anagram(first_string, second_string):
    list_1 = list(first_string.lower())
    list_2 = list(second_string.lower())

    quick_sort(list_1, 0, len(list_1) - 1)
    quick_sort(list_2, 0, len(list_2) - 1)

    if (first_string or second_string) != "":
        return ("".join(list_1), "".join(list_2), list_1 == list_2)

    return (first_string, second_string, False)


def quick_sort(list, init, end):
    if init < end:
        p = partition(list, init, end)
        quick_sort(list, init, p - 1)
        quick_sort(list, p + 1, end)


def partition(list, start, end):
    pivot = list[end]
    delimiter = start - 1

    for index in range(start, end):
        if list[index] <= pivot:
            delimiter = delimiter + 1
            list[index], list[delimiter] = list[delimiter], list[index]

    list[delimiter + 1], list[end] = list[end], list[delimiter + 1]

    return delimiter + 1
