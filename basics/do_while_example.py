def main() -> None:
    """
    do-while example.

    >>> i = 1
    >>> while True:
    ...     print(i, end='')
    ...     i += 1
    ...     if i == 6:
    ...         break
    12345

    >>> i = 5
    >>> while True:
    ...     print(i, end='')
    ...     i -= 1
    ...     if i == 0:
    ...         break
    54321
    """


if __name__ == "__main__":
    from doctest import testmod

    testmod()
