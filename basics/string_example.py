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
    >>> for char in my_str:
    ...     print(char, end='')
    123456

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
    >>> my_str[-3:]
    '456'
    >>> my_str[::-1]
    '654321cba'

    >>> len("")
    0
    >>> my_str = "abc123"
    >>> len(my_str)
    6

    >>> my_str = "      I love python.   "
    >>> my_str.strip()
    'I love python.'
    >>> my_str.strip().lower()
    'i love python.'
    >>> my_str.strip().upper()
    'I LOVE PYTHON.'
    >>> my_str.strip().replace("python", "u")
    'I love u.'
    >>> my_str.split()
    ['I', 'love', 'python.']
    >>> "love" in my_str
    True
    >>> "LOVE" not in my_str
    True

    >>> first_name = "Example"
    >>> last_name = "Hub"
    >>> name = first_name + last_name
    >>> name
    'ExampleHub'
    >>> name = first_name + last_name + "/Python"
    >>> name
    'ExampleHub/Python'
    >>> my_str = "6" * 3
    >>> my_str
    '666'

    >>> name = "Python"
    >>> age = 29
    >>> intro = "My name is {}. I'am {}.".format(name, age)
    >>> intro
    "My name is Python. I'am 29."

    >>> my_str = "abc"
    >>> del my_str
    >>> 'my_str' not in locals()
    True
    """


if __name__ == "__main__":
    from doctest import testmod

    testmod()
