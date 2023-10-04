def square(x: int | float) -> int | float:
    return x ** 2


def pow(x: int | float) -> int | float:
    return x ** x


def outer(x: int | float, function):
    """
    Create a closure that applies a given function to a value

    Parameters
    ----------
    x: int or float
        The initial value to be passed to the function
    function: callable
        A function that takes a single argument and returns a modified value

    Returns
    -------
    callable
        A closure function that, when called, applies the given function to the
        stored value. It returns the result of the function and updates the
        stored value.
    """
    nl_x = x

    def inner() -> float:
        nonlocal nl_x

        nl_x = function(nl_x)
        return nl_x

    return inner
