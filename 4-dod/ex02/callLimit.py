def callLimit(limit: int):
    """
    Create a decorator that limits the number of times a decorated function
    can be called.

    Parameters
    ----------
    limit: int
        The maximum allowed number of calls for the decorated function

    Returns
    -------
    callable
        A decorator function that can be used to limit the calls to a target
        function.I
    """
    count = 0

    def callLimiter(function):
        def limit_function(*args: any, **kwds: any):
            nonlocal count
            if count < limit:
                count += 1
                return function(*args, **kwds)
            else:
                print(f"Error: {function} call too many times")
        return limit_function
    return callLimiter


"""
Closure vs Decorator:

A closure is a nested function that has access to variables from its
containing/enclosing function's scope even after the outer function has
finished execution. It is essentially a function object that remembers values
in the enclosing scope, even if they are not present in memory, and to create
functions with persistent state.

Example:
def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function

closure = outer_function(10)
result = closure(5)  # Result is 15


A decorator is a design pattern that allows you to modify or extend the
behavior of functions or methods without changing their source code. Typically
applied to functions or methods using the '@' symbol, they are often used for
tasks like logging, authentication, and limiting the number of function calls.

Example:
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
"""
