"""
https://en.wikipedia.org/wiki/Quicksort
"""


def quick_sort(array, left: int = 0, right: int = None):
    """
    Quick sort algorithm.
    :param array: the array to be sorted.
    :param left: the left index of sub array.
    :param right: the right index of sub array.
    :return: sorted array

    >>> import random
    >>> array = random.sample(range(-50, 50), 10)
    >>> quick_sort(array) == sorted(array)
    True
    >>> import string
    >>> array = random.choices(string.ascii_letters + string.digits, k = 10)
    >>> quick_sort(array) == sorted(array)
    True
    >>> array = [random.uniform(-50.0, 50.0) for i in range(10)]
    >>> quick_sort(array) == sorted(array)
    True
    """
    if right is None:
        right = len(array) - 1
    if left >= right:
        return
    pivot = array[right]  # pick last element as pivot
    i = left
    j = right - 1
    while i <= j:
        while array[i] < pivot:
            i += 1
        while j >= 0 and array[j] >= pivot:
            j -= 1
        if i < j:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1
    array[i], array[right] = array[right], array[i]
    quick_sort(array, left, i - 1)
    quick_sort(array, i + 1, right)
    return array


if __name__ == "__main__":
    from doctest import testmod

    testmod()
