def my_function() -> None:
    """
    No argument, No Returns function.
    >>> my_function()
    hi
    """
    print("hi")


def add(a: int, b: int) -> int:
    """
    Add of a and b.
    >>> add(3, 3)
    6
    >>> add(3, -3)
    0
    >>> add(99, 1)
    100
    """
    return a + b


def add_more(*args):
    """
    Arbitrary Arguments

    >>> add_more(1, 2, 3)
    6
    """
    return sum(args)


def calculate(a: int, operator: str, b: int) -> int:
    """
    Simple calculator.

    >>> calculate(a = 3, operator = "+", b = 4)
    7
    >>> calculate(a = 3, operator = "-", b = 4)
    -1
    >>> calculate(a = 3, operator = "*", b = 4)
    12
    >>> calculate(a = 3, operator = "/", b = 4)
    0
    >>> calculate(a = 3, operator = "!", b = 4)
    Traceback (most recent call last):
    ...
    ValueError: Invalid operator
    """
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        return a // b
    else:
        raise ValueError("Invalid operator")


def intro(**kwargs):
    """
    >>> intro(name="Python", age = 29)
    key=name, value=Python
    key=age, value=29
    """
    for (
        key,
        value,
    ) in kwargs.items():
        print(f"key={key}, value={value}")


def print_number(number: int = 5) -> int:
    """
    Default parameter.

    >>> print_number(100)
    100
    >>> print_number()
    5
    """
    print(number)


def get_max(array):
    """
    Pass list as parameter.

    >>> get_max([1, 3, 5, 7, 9])
    9
    """
    max_value = array[0]
    for item in array:
        if item > max_value:
            max_value = item
    return max_value


def pass_function():
    """
    >>> pass_function()
    """
    pass  # do anything.


def factorial(n: int) -> int:
    """
    Recursion function.

    >>> factorial(0)
    1
    >>> factorial(1)
    1
    >>> factorial(5)
    120
    >>> factorial(6)
    720
    """
    return 1 if n == 0 or n == 1 else n * factorial(n - 1)


if __name__ == "__main__":
    from doctest import testmod

    testmod()
