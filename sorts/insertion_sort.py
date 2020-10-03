"""
https://en.wikipedia.org/wiki/Insertion_sort
"""


def insertion_sort(array):
    """
    Bubble sort algorithm.
    :param array: the array to be sorted.
    :return: sorted array.
    >>> import random
    >>> array = random.sample(range(-50, 50), 100)
    >>> insertion_sort(array) == sorted(array)
    True
    >>> import string
    >>> array = random.choices(string.ascii_letters + string.digits, k = 100)
    >>> insertion_sort(array) == sorted(array)
    True
    >>> array = [random.uniform(-50.0, 50.0) for i in range(100)]
    >>> insertion_sort(array) == sorted(array)
    True
    """
    for i in range(1, len(array)):
        j = i - 1
        key = array[i]
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        if j != i - 1:
            array[j + 1] = key
    return array


if __name__ == '__main__':
    from doctest import testmod

    testmod()
