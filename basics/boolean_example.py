def main():
    """
    Boolean example.

    >>> 3 > 4
    False
    >>> 3 == 4
    False
    >>> 3 < 4
    True
    >>> 3 < 4 < 5
    True
    >>> 3 < 4 > 5
    False

    >>> name = "Python"
    >>> age = 29
    >>> name == "Python" and age  == 29
    True

    >>> 'a' in 'abc'
    True
    >>> 'd' in 'abc'
    False
    >>> 'd' not in 'abc'
    True

    >>> isinstance(False, bool)
    True
    >>> isinstance(True, bool)
    True
    >>> isinstance(5, int)
    True
    >>> isinstance(3.14, float)
    True

    >>> bool('')
    False
    >>> bool(0)
    False
    >>> bool(None)
    False
    >>> bool(' ')
    True
    >>> bool(1)
    True
    >>> bool("hi")
    True
    >>> bool([])
    False
    >>> bool([''])
    True
    """


if __name__ == "__main__":
    from doctest import testmod

    testmod()
