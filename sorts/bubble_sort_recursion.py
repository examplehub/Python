"""
https://en.wikipedia.org/wiki/Bubble_sort
"""


def bubble_sort(array, length: int = 0):
    """
    :param array: the array to be sorted.
    :param length: the length of array.
    :return: sorted array.
    >>> import random
    >>> array = random.sample(range(-50, 50), 100)
    >>> bubble_sort(array) == sorted(array)
    True
    >>> import string
    >>> array = random.choices(string.ascii_letters + string.digits, k = 100)
    >>> bubble_sort(array) == sorted(array)
    True
    >>> array = [random.uniform(-50.0, 50.0) for i in range(100)]
    >>> bubble_sort(array) == sorted(array)
    True
    """
    length = length or len(array)
    swapped = False
    for i in range(length - 1):
        if array[i] > array[i + 1]:
            array[i], array[i + 1] = (
                array[i + 1],
                array[i],
            )
            swapped = True
    return array if not swapped else bubble_sort(array, length - 1)


if __name__ == "__main__":
    from doctest import testmod

    testmod()
