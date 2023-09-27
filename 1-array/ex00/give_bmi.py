import numpy


def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """
    Function uses NumPy to calculate BMI for corresponding elements in height
    and weight arrays without the need for loops

    Parameters
    ----------
    height: list
        List containing height values in int or float
    weight: list
        List containing weight values in int or float

    Returns
    -------
    list
        List of bmi values resulting from the calculation between height and
        width
    """
    if len(height) != len(weight):
        raise AssertionError("length of height and weight does not match")
    elif any(x <= 0.0 for x in height) or any(y <= 0.0 for y in weight):
        raise AssertionError("weight or length cannot be zero or negative")
    try:
        height_array = numpy.array(height)
        weight_array = numpy.array(weight)
        bmi = weight_array / (height_array ** 2)
        return bmi.tolist()
    except TypeError:
        print("TypeError: numbers only")


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Apply a limit to a list of BMI values and return a list of booleans
    indicating whether the corresponding BMI values are above the specified
    limit.

    Parameters
    ----------
    bmi: list
        List of BMI values either as int or floats
    limit: float
        The BMI limit to compare against

    Returns
    -------
    list
        A list of booleans, where each element is True if the corresponding
        BMI value is above the limit, and vice versa.
    """
    try:
        bmi_array = numpy.array(bmi)
        return (bmi_array > limit).tolist()
    except TypeError:
        print("TypeError: bmi (first argument) must contains only list of int")


height = [1.71, 1.65, 1.73, 1.95, 1.63]
weight = [65.3, 58.4, 63.4, 94.5, 72.9]
bmi = give_bmi(height, weight)
print(bmi, type(bmi))
print(apply_limit(bmi, 26))