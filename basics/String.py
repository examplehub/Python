if __name__ == '__main__':
    # output: ExampleHub
    print("ExampleHub")

    # output: ExampleHub
    my_str = "ExampleHub"
    print(my_str)

    """
    output:
    Python is an interpreted, high-level and 
    general-purpose programming language.
    Created by Guido van Rossum and first released in 1991, 
    Python's design philosophy emphasizes code readability 
    with its notable use of significant whitespace.    
    """
    my_str = """
Python is an interpreted, high-level and 
general-purpose programming language.
Created by Guido van Rossum and first released in 1991, 
Python's design philosophy emphasizes code readability 
with its notable use of significant whitespace. 
    """
    print(my_str)

    my_str = "abc"
    assert my_str[0] == 'a'
    assert my_str[1] == 'b'
    assert my_str[2] == 'c'
    assert my_str[-1] == 'c'

    my_str = "123456"
    for i in range(0, 6):
        assert my_str[i] == str(i + 1)

    my_str = "abc123456"
    assert my_str[0:3] == "abc"
    assert my_str[:3] == "abc"
    assert my_str[3:9] == "123456"
    assert my_str[3:] == "123456"

    assert my_str[-3:-1] == "45"
    assert my_str[-3:0] == "456"
