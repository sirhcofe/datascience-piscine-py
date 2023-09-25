def rotate(zoomed_image, rotation):
    """
    Rotates image at 90 degrees for specified times

    Parameters
    ----------
    zoomed_image: numpy.ndarray
        An array representing the zoomed image's pixel properties
    rotation: int
        The number of times to rotate the image in 90 degrees

    Returns
    -------
    numpy.ndarray
        The NumPy array representing the rotated image's pixel properties
    """

    # Convert rotation count to degrees, and simplify large numbers
    rot_angle = (rotation * 90) % 360
    rot_angle = (rot_angle + 360) if rot_angle < 0 else rot_angle
    w = zoomed_image.shape[1]
    h = zoomed_image.shape[0]

    # Reshape back to 2D array
    zoomed_image = np.reshape(zoomed_image, (h, w))

    # Create new image array
    if rot_angle % 180 == 0:
        rot_image = zoomed_image.copy()
    else:
        rot_image = np.zeros((w, h))

    # Get new rotated image size
    r_w = rot_image.shape[1]
    r_h = rot_image.shape[0]

    # Loop to transpose each pixel
    for row in range(r_h):
        for col in range(r_w):
            if (rot_angle == 90):
                rot_image[row][col] = zoomed_image[h - col - 1][row]
            elif (rot_angle == 180):
                rot_image[row][col] = zoomed_image[h - row - 1][w - col - 1]
            elif (rot_angle == 270):
                rot_image[row][col] = zoomed_image[col][w - row - 1]
    return (rot_image)


def zoom_image(image_data, scale):
    """
    Zooms and convert image to grayscale

    Parameters
    ----------
    image_data: numpy.ndarray
        An array representing the image's pixel properties
    scale: int
        The scaling factor for zooming the image

    Returns
    -------
    numpy.ndarray
        The NumPy array representing the zoomed image's pixel properties
    """
    height, width = image_data.shape[0], image_data.shape[1]
    new_height, new_width = round(height // scale), round(width // scale)
    start_h_index = round((height - new_height) / 2)
    start_w_index = round((width - new_width) / 2)
    zoomed_image = image_data[
        start_h_index:(start_h_index + new_height),
        start_w_index:(start_w_index + new_width)
    ]
    grayscale = np.reshape(
        np.mean(zoomed_image, axis=2).astype(int),
        (new_height, new_width, 1)
    )
    return (grayscale)


def zoom_and_rotate(image_data, scale, rotation):
    if not isinstance(image_data, np.ndarray):
        raise ValueError("image_data must be a NumPy array")
    elif not isinstance(scale, (int, float)) or scale <= 0:
        raise ValueError("scale must be a positive int/float")
    elif not isinstance(rotation, int):
        raise ValueError("rotation angle must be an integer")
    zoomed_image = zoom_image(image_data, scale)
    print(
        f"New shape after slicing: {zoomed_image.shape}"
        f" or {zoomed_image.shape[:2]}"
    )
    print(zoomed_image)
    rotated_image = rotate(zoomed_image, rotation)
    print(f"New shape after transpose: {rotated_image.shape}")
    print(rotated_image)
    plt.imshow(rotated_image, cmap="grey")
    plt.savefig('rotated_image.jpeg', bbox_inches='tight')


def main():
    """Main function"""
    image_data = ft_load("animal.jpeg")
    scale = 2
    rotation = -10
    if image_data is not None:
        zoom_and_rotate(image_data, scale, rotation)


if __name__ == "__main__":
    import numpy as np
    import matplotlib.pyplot as plt
    from load_image import ft_load
    main()
