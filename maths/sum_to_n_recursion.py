def sum_to_n_recursion(number: int) -> int:
    """
    >>> sum_to_n_recursion(0)
    0
    >>> sum_to_n_recursion(10)
    55
    >>> sum_to_n_recursion(100)
    5050
    """
    return 0 if number == 0 else number + sum_to_n_recursion(number - 1)


if __name__ == '__main__':
    from doctest import testmod

    testmod()
