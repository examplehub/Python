"""
https://en.wikipedia.org/wiki/Bubble_sort
"""


def bubble_sort(array):
    """
    >>> import random
    >>> array = random.sample(range(-50, 50), 100)
    >>> bubble_sort(array) == sorted(array)
    True
    >>> import string
    >>> array = random.choices(string.ascii_letters + string.digits, k = 100)
    >>> bubble_sort(array) == sorted(array)
    True
    """
    length = len(array)
    for i in range(0, length - 1):
        swapped = False
        for j in range(0, length - 1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True
        if not swapped:
            break
    return array


if __name__ == '__main__':
    from doctest import testmod

    testmod()
