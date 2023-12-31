def mean(data):
    """
    Calculate the mean (average) of a list of data

    Parameters
    ----------
    data: list of int or float
        The input data

    Returns
    -------
    float
        The mean of the data
    """
    return sum(data) / len(data)


def median(data):
    """
    Calculate the meadian of a list of data

    Parameters
    ----------
    data: list of int or float
        The input data

    Returns
    -------
    float
        The median value of the data
    """
    n = len(data)
    middle = n // 2
    if n % 2 == 0:
        return (data[middle - 1] + data[middle]) / 2
    else:
        return data[middle]


def quartile(data):
    """
    Calculate the quartiles (25th and 75th percentiles)

    Parameters
    ----------
    data: list of int or float
        The input data

    Returns
    -------
    tuple
        A tuple containing the 25th and 75th percentiles of the data
    """
    n = len(data)
    quartile_25 = round(0.25 * (n + 1)) - 1
    quartile_75 = round(0.75 * (n + 1)) - 1
    return data[quartile_25], data[quartile_75]


def variance(data):
    """
    Calculate the variance of a list of data

    Parameters
    ----------
    data: list of int or float
        The input data

    Returns
    -------
    float
        The variance of the data
    """
    n = len(data)
    if n == 0:
        return 0
    mean_value = mean(data)
    squared_diff_sum = sum((x - mean_value) ** 2 for x in data)
    return squared_diff_sum / n


def standard_deviation(data):
    """
    Calculate the standatd deviation of a list of data

    Parameters
    ----------
    data: list of int or float
        The input data

    Returns
    -------
    float
        The standard deviation of the data
    """
    var = variance(data)
    if var == 0:
        return 0
    return var ** 0.5


def ft_statistics(*args, **kwargs):
    """
    Calculate and print various statistics of the input data

    Parameters
    ----------
    *args:
        Variable number of data points
    **kwargs:
        Keyword arguments specifying the statistics to calculate
    """
    data = sorted(list(args))

    for key, value in kwargs.items():
        if not args:
            print("ERROR")
        elif value == "mean":
            print(f"mean: {mean(data):.1f}")
        elif value == "median":
            print(f"median: {median(data)}")
        elif value == "quartile":
            q25, q75 = quartile(data)
            print(f"quartile: [{q25:.1f}, {q75:.1f}]")
        elif value == "std":
            print(f"std: {standard_deviation(data)}")
        elif value == "var":
            print(f"var: {variance(data)}")
        else:
            continue
