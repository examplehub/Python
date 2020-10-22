def main():
    """
    >>> a = 3
    >>> b = 4
    >>> a + b
    7
    >>> a - b
    -1
    >>> a * b
    12
    >>> a / b
    0.75
    >>> a // b
    0
    >>> a % b
    3
    >>> 3 ** 4
    81

    >>> type(3)
    <class 'int'>
    >>> type(3.14)
    <class 'float'>
    >>> type('a')
    <class 'str'>
    >>> type("abc")
    <class 'str'>
    >>> type(True)
    <class 'bool'>
    >>> type(None)
    <class 'NoneType'>
    >>> type(3 + 4j)
    <class 'complex'>

    >>> int(3.14)
    3
    >>> int(-3)
    -3
    >>> float("3.14")
    3.14
    >>> str(3.14)
    '3.14'
    >>> str(3 + 4j)
    '(3+4j)'
    >>> chr(65)
    'A'
    >>> chr(97)
    'a'
    >>> ord("a")
    97
    >>> ord("A")
    65
    >>> chr(ord('a') - 32)
    'A'
    >>> chr(ord('A') + 32)
    'a'
    """


if __name__ == "__main__":
    from doctest import testmod

    testmod()
