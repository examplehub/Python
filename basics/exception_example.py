def divide(a: int, b: int) -> int:
    """
    >>> divide(10, 2)
    5
    >>> divide(10, 0)
    Traceback (most recent call last):
    ...
    ValueError: divisor can't be zero
    """
    try:
        return a // b
    except ArithmeticError:
        raise ValueError("divisor can't be zero")
    finally:
        pass  # do anything you want.


if __name__ == "__main__":
    from doctest import testmod

    testmod()
