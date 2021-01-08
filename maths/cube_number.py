"""
https://en.wikipedia.org/wiki/Cube_(algebra)
"""


def is_cube_number(number: int) -> bool:
    """
    >>> all(is_cube_number(num) for num in [-8, -1, 0, 1, 8, 27, 64, 8000, 216_000])
    True
    >>> is_cube_number(4)
    False
    >>> is_cube_number(11)
    False
    >>> is_cube_number(2**20)
    False
    """
    number = abs(number)
    for i in range(0, number + 1):
        if i ** 3 == number:
            return True
        if i ** 3 > number:
            return False
    return False


if __name__ == "__main__":
    from doctest import testmod

    testmod()
