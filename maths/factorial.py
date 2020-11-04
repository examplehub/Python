def factorial(number: int) -> int:
    """
    >>> factorial(5)
    120
    >>> factorial(0)
    1
    >>> import random
    >>> import math
    >>> numbers = list(range(0, 50))
    >>> for num in numbers:
    ...     assert factorial(num) == math.factorial(num)
    >>> factorial(-1)
    Traceback (most recent call last):
    ...
    ValueError: factorial() not defined for negative values
    """
    if number < 0:
        raise ValueError("factorial() not defined for negative values")
    fact = 1
    for i in range(1, number + 1):
        fact *= i
    return fact


if __name__ == "__main__":
    from doctest import testmod

    testmod()
