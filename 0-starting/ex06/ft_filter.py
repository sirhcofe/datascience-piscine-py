def ft_filter(function, iterable):
    """filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""

    # List comprehension is a concise and readable way to create lists in
    # Python. It allows creating a new list by specifying its elements using a
    # single line of code. The syntax is as follow:
    # new_list = [expression for item in iterable if condition]
    return [
        index for index in iterable
        if (function(index) if function else index)
    ]
