from typing import Any


class Stack:
    def __init__(self, capacity: int = 10) -> None:
        self.stack = []
        self.capacity = capacity

    def __len__(self):
        """
        >>> stack = Stack()
        >>> for i in range(0, 10):
        ...     stack.push(i)
        >>> len(stack)
        10
        """
        return len(self.stack)

    def size(self) -> int:
        """
        >>> stack = Stack()
        >>> for i in range(0, 10):
        ...     assert len(stack) == i
        ...     stack.push(i)
        >>> stack.size()
        10
        """
        return len(self)

    def is_full(self) -> bool:
        """
        >>> stack = Stack()
        >>> for i in range(0, 10):
        ...     stack.push(i)
        >>> stack.is_full()
        True
        """
        return len(self) == self.capacity

    def is_empty(self) -> bool:
        """
        >>> stack = Stack()
        >>> stack.is_empty()
        True
        >>> stack.push(666)
        >>> stack.push(999)
        >>> stack.is_empty()
        False
        """
        return len(self) == 0

    def push(self, item: Any) -> None:
        """
        >>> stack = Stack()
        >>> for i in range(0, 10):
        ...     stack.push(i)
        >>> stack.push(666)
        Traceback (most recent call last):
        ...
        ValueError: stack is full
        """
        if self.is_full():
            raise ValueError("stack is full")
        self.stack.append(item)

    def pop(self) -> Any:
        """
        >>> stack = Stack()
        >>> stack.pop()
        Traceback (most recent call last):
        ...
        ValueError: stack is empty
        >>> for i in range(0, 10):
        ...     stack.push(i)
        >>> for i in range(9, -1, -1):
        ...     assert stack.pop() == i
        """
        if self.is_empty():
            raise ValueError("stack is empty")
        return self.stack.pop()

    def peek(self) -> Any:
        """
        >>> stack = Stack()
        >>> stack.peek()
        Traceback (most recent call last):
        ...
        ValueError: stack is empty
        >>> stack.push('a')
        >>> stack.push('b')
        >>> stack.push('c')
        >>> stack.peek()
        'c'
        """
        if self.is_empty():
            raise ValueError("stack is empty")
        return self.stack[-1]


if __name__ == "__main__":
    from doctest import testmod

    testmod()
