def main() -> None:
    """
    for example.

    >>> for item in ["Python", "Java", "Google"]:
    ...     print(item)
    Python
    Java
    Google

    >>> for char in "Python":
    ...     print(char, end='')
    Python

    >>> for i in range(0, 6):
    ...     print(i, end='')
    012345

    >>> for i in range(1, 10, 2):
    ...     print(i, end='')
    13579

    >>> for i in range(0, 6):
    ...     print(i, end='')
    ... else:
    ...     print(6, end='')
    0123456

    >>> for i in range(0, 3):
    ...     for j in range(0, 3):
    ...         print(f"i={i}, j={j}")
    i=0, j=0
    i=0, j=1
    i=0, j=2
    i=1, j=0
    i=1, j=1
    i=1, j=2
    i=2, j=0
    i=2, j=1
    i=2, j=2

    >>> for _ in range(0, 100):
    ...     pass

    >>> sum(i for i in range(1, 101))
    5050

    >>> for i in range(1, 6):
    ...     for _ in range(1, i + 1):
    ...         print("*", end='')
    ...     print()
    *
    **
    ***
    ****
    *****
    """


if __name__ == "__main__":
    from doctest import testmod

    testmod()
