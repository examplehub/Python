def sum_to_n(n: int) -> int:
    """
    >>> sum_to_n(100)
    5050
    >>> sum_to_n(10)
    55
    """
    return sum(i for i in range(1, n + 1))


if __name__ == "__main__":
    from doctest import testmod

    testmod()
