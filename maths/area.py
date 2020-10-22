def circle_area(radius: float) -> float:
    """
    >>> circle_area(10)
    314.1592653589793
    >>> circle_area(0)
    0.0
    """
    import math
    return math.pi * radius * radius


if __name__ == "__main__":
    from doctest import testmod

    testmod()
