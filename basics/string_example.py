def main():
    """
    >>> print("ExampleHub")
    ExampleHub
    >>> my_str = "ExampleHub"
    >>> print(my_str)
    ExampleHub
    >>> my_str = "abc"
    >>> my_str[0]
    'a'
    >>> my_str[1]
    'b'
    >>> my_str[2]
    'c'
    >>> my_str[-1]
    'c'
    >>> my_str = "123456"
    >>> for i in range(0, 6):
    ...     assert my_str[i] == str(i + 1)
    >>> my_str = "abc123456"
    >>> my_str[0:3]
    'abc'
    >>> my_str[:3]
    'abc'
    >>> my_str[3:9]
    '123456'
    >>> my_str[3:]
    '123456'
    >>> my_str[-3:-1]
    '45'
    >>> my_str[-3:0]
    '456'
    """


if __name__ == '__main__':
    from doctest import testmod

    testmod()
