def main():
    """
    >>> array = range(0, 5)
    >>> iterator = iter(array)
    >>> for item in iterator:
    ...     print(item, end='')
    01234

    >>> iterator = iter(array)
    >>> next(iterator)
    0
    >>> next(iterator)
    1
    >>> next(iterator)
    2
    >>> next(iterator)
    3
    >>> next(iterator)
    4
    >>> next(iterator)
    Traceback (most recent call last):
    ...
    StopIteration
    """


class Counter:
    """
    >>> counter = Counter(5)
    >>> iterator = iter(counter)
    >>> for item in iterator:
    ...     print(item)
    1
    2
    3
    4
    5
    """

    def __init__(self, count):
        self.count = count

    def __iter__(self):
        self.num = 1
        return self

    def __next__(self):
        if self.num <= self.count:
            temp = self.num
            self.num += 1
            return temp
        else:
            raise StopIteration


class InfiniteCounter:
    def __init__(self):
        self.num = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.num += 1
        return self.num


if __name__ == "__main__":
    from doctest import testmod

    testmod()

    # counter = InfiniteCounter()
    # for item in iter(counter):
    #     print(item)
