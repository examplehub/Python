"""
https://en.wikipedia.org/wiki/Fahrenheit
"""


def fahrenheit_to_celsius(temperature: float) -> float:
    """
    >>> fahrenheit_to_celsius(32)
    0.0
    >>> fahrenheit_to_celsius(39)
    3.888888888888889
    """
    return 5 * (temperature - 32) / 9


if __name__ == '__main__':
    from doctest import testmod

    testmod()
