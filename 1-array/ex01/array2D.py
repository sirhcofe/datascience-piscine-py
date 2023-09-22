import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
    Slice a 2D array and return a truncated version based on start and end
    indices.

    Parameters
    ----------
    family: list of lists
        A 2D array represented as a list of lists
    start: int
        The starting index for slicing (count from right if value is negative)
    end: int
        The ending index for slicing (count from right if value is negative)

    Returns
    -------
    list of lists
        A truncated 2D array containing rows from start to end
    """
    if not isinstance(family, list):
        raise AssertionError("family (first argument) must be a list")
    elif not isinstance(start, int) or not isinstance(end, int):
        raise AssertionError("start and end indices must be integer")
    try:
        array = np.array(family)
        print(f"My shape is: {array.shape}")
        new_array = array[start:end]
        print(f"My new shape is: {new_array.shape}")
        return (new_array.tolist())
    except ValueError as e:
        print(f"ValueError: {e}")
