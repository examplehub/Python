def main() -> None:
    """
    >>> from collections import deque
    >>> queue = deque(["Python", "Java", "C"])
    >>> len(queue)
    3
    >>> queue
    deque(['Python', 'Java', 'C'])
    >>> queue.popleft()
    'Python'
    >>> queue.popleft()
    'Java'
    >>> queue.clear()
    >>> len(queue)
    0
    >>> queue
    deque([])
    >>> queue.popleft()
    Traceback (most recent call last):
    ...
    IndexError: pop from an empty deque
    """


if __name__ == '__main__':
    from doctest import testmod

    testmod()
