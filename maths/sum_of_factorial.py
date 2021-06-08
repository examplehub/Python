def sum_of_factorial(number: int) -> int:
    """
    >>> sum_of_factorial(0)
    0
    >>> sum_of_factorial(1)
    1
    >>> sum_of_factorial(2)
    3
    >>> sum_of_factorial(5)
    153
    """
    sum_factorial = 0
    factorial = 1
    for i in range(1, number + 1):
        factorial *= i
        sum_factorial = sum_factorial + factorial

    return sum_factorial


def sum_of_factorial_circle_plus_recursion(number: int) -> int:
    """
    >>> sum_of_factorial_circle_plus_recursion(0)
    0
    >>> sum_of_factorial_circle_plus_recursion(1)
    1
    >>> sum_of_factorial_circle_plus_recursion(2)
    3
    >>> sum_of_factorial_circle_plus_recursion(5)
    153
    """
    sum_factorial = 0
    from math import factorial

    for i in range(1, number + 1):
        sum_factorial += factorial(i)
    return sum_factorial


def sum_of_factorial_pure_recursion(number: int) -> int:
    """
    >>> sum_of_factorial_pure_recursion(0)
    0
    >>> sum_of_factorial_pure_recursion(1)
    1
    >>> sum_of_factorial_pure_recursion(2)
    3
    >>> sum_of_factorial_pure_recursion(5)
    153
    """
    if number == 1 or number == 0:
        return number  # 1! or 0!
    elif number == 2:
        return 3  # 1! + 2!
    else:
        return (
            sum_of_factorial_pure_recursion(number - 1)
            + (
                sum_of_factorial_pure_recursion(number - 1)
                - sum_of_factorial_pure_recursion(number - 2)
            )
            * number
        )


if __name__ == "__main__":
    from doctest import testmod

    testmod()
