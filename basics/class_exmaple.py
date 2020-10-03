class People:
    """
    >>> jack = People("Jack", 23)
    >>> jack.name
    'Jack'
    >>> jack.age
    23
    >>> jack.print_info()
    my name is Jack, my age is 23
    >>> jack.age += 1
    >>> jack.age
    24
    >>> del jack.age
    >>> hasattr(jack, "age")
    False
    >>> del jack
    >>> "jack" in locals()
    False
    """

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_info(self):
        print(f"my name is {self.name}, my age is {self.age}")


class Student(People):
    """
    >>> stu = Student("Tom", 19, 99)
    >>> stu.print_info()
    my name is Tom, my age is 19, my grade is 99
    """
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

    def print_info(self):
        print(f"my name is {self.name}, my age is {self.age}, my grade is {self.grade}")


class TodoClass:
    pass


if __name__ == '__main__':
    from doctest import testmod

    testmod()
