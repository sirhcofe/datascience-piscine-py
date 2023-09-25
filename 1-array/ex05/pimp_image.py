import numpy as np
import matplotlib.pyplot as plt


def verify_and_parse(array):
    """
    Verify if 'array' is a NumPy array and parse its RGB(A) channels.

    Parameters
    ----------
    array: numpy.ndarray
        Input image data

    Returns
    -------
    tuple
        A tuple containing the r, g, b, and alpha channel, which are NumPy
        arrays
    """
    if not isinstance(array, np.ndarray):
        raise AssertionError("not an array")
    r = array[:, :, 0]
    g = array[:, :, 1]
    b = array[:, :, 2]
    if array.shape[2] == 4:
        a = array[:, :, 3]
    else:
        a = np.full((array.shape[0], array.shape[1]), 255)
    return (r, g, b, a)


def ft_invert(array) -> np.ndarray:
    """
    Invert the colors of an RGB(A) image

    Parameters
    ----------
    array: numpy.ndarray
        Input image data

    Returns
    -------
    numpy.ndarray
        Inverted image data
    """
    r, g, b, a = verify_and_parse(array)
    invert_r = 255 - r
    invert_g = 255 - g
    invert_b = 255 - b
    inverted = np.stack((invert_r, invert_g, invert_b, a), axis=-1)
    plt.imshow(inverted)
    plt.savefig('inverted.jpeg', bbox_inches='tight')
    return (inverted)


def ft_red(array) -> np.ndarray:
    """
    Extract only the red channel from an RGB(A) image

    Parameters
    ----------
    array: numpy.ndarray
        Input image data

    Returns
    -------
    numpy.ndarray
        Image data with only the red channel
    """
    r, g, b, a = verify_and_parse(array)
    no_g = g * 0
    no_b = b * 0
    only_red = np.stack((r, no_g, no_b, a), axis=-1)
    plt.imshow(only_red)
    plt.savefig('only_red.jpeg', bbox_inches='tight')
    return (only_red)


def ft_blue(array) -> np.ndarray:
    """
    Extract only the blue channel from an RGB(A) image

    Parameters
    ----------
    array: numpy.ndarray
        Input image data

    Returns
    -------
    numpy.ndarray
        Image data with only the blue channel
    """
    row = array.shape[0]
    col = array.shape[1]
    r, g, b, a = verify_and_parse(array)
    no_r = [[0 for _ in range(col)] for _ in range(row)]
    no_g = [[0 for _ in range(col)] for _ in range(row)]
    only_blue = np.stack((no_r, no_g, b, a), axis=-1)
    plt.imshow(only_blue)
    plt.savefig('only_blue.jpeg', bbox_inches='tight')
    return (only_blue)


def ft_green(array) -> np.ndarray:
    """
    Extract only the green channel from an RGB(A) image

    Parameters
    ----------
    array: numpy.ndarray
        Input image data

    Returns
    -------
    numpy.ndarray
        Image data with only the green channel
    """
    r, g, b, a = verify_and_parse(array)
    no_r = r - r
    no_b = b - b
    only_green = np.stack((no_r, g, no_b, a), axis=-1)
    plt.imshow(only_green)
    plt.savefig('only_green.jpeg', bbox_inches='tight')
    return (only_green)


def ft_grey(array) -> np.ndarray:
    """
    Convert an RGB(A) image to grayscale using luminance weights

    Paarameters
    -----------
    array: numpy.ndarray
        Input image data

    Returns
    -------
    numpy.ndarray
        Grayscale image data
    """
    greyscale = np.round(np.dot(array[:, :, :3], [0.3, 0.59, 0.11]))
    plt.imshow(greyscale, cmap="gray")
    plt.savefig('only_greyscale.jpeg', bbox_inches='tight')
    return (greyscale)
