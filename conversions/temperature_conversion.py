"""
https://en.wikipedia.org/wiki/Fahrenheit
https://en.wikipedia.org/wiki/Celsius
"""


def fahrenheit_to_celsius(temperature: float) -> float:
    """
    >>> fahrenheit_to_celsius(32)
    0.0
    >>> fahrenheit_to_celsius(39)
    3.89
    """
    return round(5 * (temperature - 32) / 9, 2)


def celsius_to_fahrenheit(temperature: float) -> float:
    """
    >>> celsius_to_fahrenheit(0)
    32.0
    >>> celsius_to_fahrenheit(30.5)
    86.9
    """
    return round((temperature * 9 / 5) + 32, 2)


if __name__ == "__main__":
    from doctest import testmod

    testmod()
