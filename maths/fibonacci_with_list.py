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
    fibs = [0] * (number + 2)
    fibs[0] = 0
    fibs[1] = 1
    for i in range(2, number + 1):
        fibs[i] = fibs[i - 1] + fibs[i - 2]
    return fibs[number]


if __name__ == "__main__":
    from doctest import testmod

    testmod()
