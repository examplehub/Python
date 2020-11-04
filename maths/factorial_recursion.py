def factorial_recursion(number: int) -> int:
    """
    >>> factorial_recursion(5)
    120
    >>> factorial_recursion(0)
    1
    >>> import random
    >>> import math
    >>> numbers = list(range(0, 50))
    >>> for num in numbers:
    ...     assert factorial_recursion(num) == math.factorial(num)
    >>> factorial_recursion(-1)
    Traceback (most recent call last):
    ...
    ValueError: factorial() not defined for negative values
    """
    if number < 0:
        raise ValueError("factorial() not defined for negative values")
    return (
        1 if number == 0 or number == 1
        else number * factorial_recursion(number - 1)
    )


if __name__ == '__main__':
    from doctest import testmod

    testmod()
