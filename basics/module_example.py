def main() -> None:
    """
    >>> import math
    >>> math.pow(2, 3) == 8
    True

    >>> from sorts.bubble_sort import bubble_sort
    >>> bubble_sort([1, 3, 5, 2, 4]) == sorted([1, 3, 5, 2, 4])
    True

    >>> from sorts.selection_sort import selection_sort as sort
    >>> sort(['a', 'c', 'd', 'b'])
    ['a', 'b', 'c', 'd']

    """


if __name__ == '__main__':
    from doctest import testmod

    testmod()
