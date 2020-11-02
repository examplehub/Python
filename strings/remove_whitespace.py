def remove_whitespace(original: str) -> str:
    """
    >>> remove_whitespace("I Love Python")
    'ILovePython'
    >>> remove_whitespace("I    Love       Python")
    'ILovePython'
    >>> remove_whitespace('    I     Love     Python')
    'ILovePython'
    >>> remove_whitespace("")
    ''
    """
    return "".join(original.split())


def remove_whitespace2(original: str) -> str:
    """
    >>> remove_whitespace2("I Love Python")
    'ILovePython'
    >>> remove_whitespace2("I    Love       Python")
    'ILovePython'
    >>> remove_whitespace2('    I     Love     Python')
    'ILovePython'
    >>> remove_whitespace2("")
    ''
    """
    return original.replace(" ", "")


if __name__ == '__main__':
    from doctest import testmod

    testmod()
