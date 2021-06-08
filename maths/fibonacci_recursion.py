def fibonacci(number: int) -> int:
    """
    >>> fibonacci(0)
    0
    >>> fibonacci(1)
    1
    >>> fibonacci(2)
    1
    >>> fibonacci(3)
    2
    >>> fibonacci(4)
    3
    >>> fibonacci(5)
    5
    >>> fibonacci(6)
    8
    >>> fibonacci(7)
    13
    >>> fibonacci(8)
    21
    """
    return number if number == 0 or number == 1 else fibonacci(number - 1) + fibonacci(number - 2)


if __name__ == "__main__":
    from doctest import testmod

    testmod()
