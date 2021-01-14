"""
https://en.wikipedia.org/wiki/Shellsort
"""


def shell_sort(array):
    """
    Shell Sort algorithm
    :param array: the array to be sorted.
    :return: sorted array.
    >>> import random
    >>> array = random.sample(range(-50, 50), 100)
    >>> shell_sort(array) == sorted(array)
    True
    >>> import string
    >>> array = random.choices(string.ascii_letters + string.digits, k = 100)
    >>> shell_sort(array) == sorted(array)
    True
    >>> array = [random.uniform(-50.0, 50.0) for i in range(100)]
    >>> shell_sort(array) == sorted(array)
    True
    """
    gap = len(array) >> 1
    while gap > 0:
        for i in range(gap, len(array)):
            insert_value = array[i]
            j = i - gap
            while j >= 0 and insert_value < array[j]:
                array[j + gap] = array[j]
                j -= gap
            if j != i - gap:
                array[j + gap] = insert_value
        gap >>= 1
    return array


if __name__ == "__main__":
    from doctest import testmod

    testmod()
