"""
https://en.wikipedia.org/wiki/Queue_(abstract_data_type)
"""
from typing import Any


class Queue:
    def __init__(self) -> None:
        self.queue = []

    def __len__(self) -> int:
        """
        >>> queue = Queue()
        >>> len(queue)
        0
        >>> for i in range(0, 5):
        ...     assert len(queue) == i
        ...     queue.enqueue(i)
        >>> len(queue)
        5
        """
        return len(self.queue)

    def __str__(self) -> str:
        """
        >>> queue = Queue()
        >>> str(queue)
        ''
        >>> for i in range(1, 6):
        ...     queue.enqueue(i)
        >>> str(queue)
        '1 <- 2 <- 3 <- 4 <- 5'
        """
        return " <- ".join([str(item) for item in self.queue])

    def size(self) -> int:
        """
        >>> queue = Queue()
        >>> queue.size()
        0
        >>> for i in range(0, 5):
        ...     assert queue.size() == i
        ...     queue.enqueue(i)
        >>> queue.size()
        5
        """
        return len(self)

    def is_empty(self) -> bool:
        """
        >>> queue = Queue()
        >>> queue.is_empty()
        True
        >>> queue.enqueue('a')
        >>> queue.enqueue('b')
        >>> queue.is_empty()
        False
        """
        return len(self) == 0

    def enqueue(self, item: Any) -> None:
        """
        >>> queue = Queue()
        >>> str(queue)
        ''
        >>> for i in range(0, 5):
        ...     queue.enqueue(i)
        >>> str(queue)
        '0 <- 1 <- 2 <- 3 <- 4'
        """
        self.queue.append(item)

    def dequeue(self) -> Any:
        """
        >>> queue = Queue()
        >>> for i in range(0, 5):
        ...     queue.enqueue(i)
        >>> str(queue)
        '0 <- 1 <- 2 <- 3 <- 4'
        >>> queue.dequeue()
        0
        >>> queue.dequeue()
        1
        >>> str(queue)
        '2 <- 3 <- 4'
        >>> for i in range(2, 5):
        ...     assert queue.dequeue() == i
        >>> str(queue)
        ''
        """
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        ret_item = self.queue[0]
        self.queue = self.queue[1:]
        return ret_item

    def peek(self) -> Any:
        """
        >>> queue = Queue()
        >>> queue.enqueue("Python")
        >>> queue.enqueue("Java")
        >>> queue.enqueue("C")
        >>> queue.peek()
        'Python'
        >>> queue.dequeue()
        'Python'
        >>> queue.dequeue()
        'Java'
        """
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self.queue[0]

    def clear(self) -> None:
        """
        >>> queue = Queue()
        >>> for i in range(1, 6):
        ...     queue.enqueue(i)
        >>> str(queue)
        '1 <- 2 <- 3 <- 4 <- 5'
        >>> queue.clear()
        >>> str(queue)
        ''
        """
        self.queue = []


if __name__ == "__main__":
    from doctest import testmod

    testmod()
