def circle_area(radius: float) -> float:
    """
    >>> circle_area(10)
    314.1592653589793
    >>> circle_area(0)
    0.0
    """
    import math

    return math.pi * radius * radius


def rectangle_area(length: float, width: float) -> float:
    """
    >>> rectangle_area(3, 4)
    12
    >>> rectangle_area(3, 0)
    0
    >>> rectangle_area(0, 4)
    0
    """
    return length * width


def square_area(length: float) -> float:
    """
    >>> square_area(4)
    16
    >>> square_area(0)
    0
    """
    return length ** 2


def triangle_area(length: float, height: float) -> float:
    """
    >>> triangle_area(3, 4)
    6.0
    >>> triangle_area(3, 0)
    0.0
    >>> triangle_area(0, 4)
    0.0
    """
    return length * height / 2


if __name__ == "__main__":
    from doctest import testmod

    testmod()
