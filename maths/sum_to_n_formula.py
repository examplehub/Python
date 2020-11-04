def sum_to_n(n: int) -> int:
    """
    >>> sum_to_n(0)
    0
    >>> sum_to_n(1)
    1
    >>> sum_to_n(2)
    3
    >>> sum_to_n(10)
    55
    >>> sum_to_n(100)
    5050
    """
    return (1 + n) * n // 2


if __name__ == "__main__":
    from doctest import testmod

    testmod()
