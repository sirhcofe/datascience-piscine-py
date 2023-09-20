def ft_filter(function, iterable):
    """
    Replica of built in `filter` function:
    filter(function or None, iterable) --> filter object
    Return an iterator yielding those items of iterable for which
    function(item) is true. If function is None, return the items that are
    true

        Parameters:
                function: An expression that filters the elements from iterable
                iterable: The sequence to iterate over (eg string)
        Return:
                filtered list
    """

    # List comprehension is a concise and readable way to create lists in
    # Python. It allows creating a new list by specifying its elements using a
    # single line of code. The syntax is as follow:
    # new_list = [expression for item in iterable if condition]
    return [
        index for index in iterable
        if (function(index) if function else index)
    ]
