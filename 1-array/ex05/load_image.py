from PIL import Image
import numpy as np


def ft_load(path: str) -> np.ndarray:
    """
    Loads an image from specified file path, and provide information about
    the image.

    Parameters
    ----------
    path: str
        Path to image

    Returns
    -------
    numpy.ndarray
        A NumPy array representing the image's pixel datas in RGB format.
    """
    try:
        im = Image.open(path)
        pixel_data = np.array(im)
        print(
            f"File format: {im.format}\n"
            f"Image resolution: {im.size}"
        )
        return (pixel_data)
    except FileNotFoundError:
        print(f"FileNotFoundError: No such file or directory: {path}")
