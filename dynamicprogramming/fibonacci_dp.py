def fibonacci(nth: int) -> int:
    """
    >>> fibonacci(0)
    0
    >>> fibonacci(1)
    1
    >>> fibonacci(2)
    1
    >>> fibonacci(9)
    34
    """
    fibs = [0] * (nth + 2)
    fibs[0] = 0
    fibs[1] = 1

    for i in range(2, nth + 1):
        fibs[i] = fibs[i - 1] + fibs[i - 2]
    return fibs[nth]


if __name__ == "__main__":
    from doctest import testmod

    testmod()
