"""
https://en.wikipedia.org/wiki/Binary_number
https://en.wikipedia.org/wiki/Decimal
"""


def binary_to_decimal(binary: str) -> int:
    """
    >>> binary_to_decimal("0")
    0
    >>> binary_to_decimal("1")
    1
    >>> binary_to_decimal("1010")
    10
    >>> binary_to_decimal("-11101")
    -29
    """
    is_negative = binary[0] == "-"
    binary = binary[1:] if is_negative else binary
    decimal = 0
    for i in range(0, len(binary)):
        decimal += int(binary[i]) * (2 ** (len(binary) - i - 1))
    return -decimal if is_negative else decimal


if __name__ == "__main__":
    from doctest import testmod

    testmod()
