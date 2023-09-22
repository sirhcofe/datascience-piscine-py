def zoom_image(image_data, scale):
    """
    Zooms and convert image to grayscale

    Parameters
    ----------
    image_data: numpy.ndarray
        An array representing the image's pixel properties
    scale: int
        The scaling factor for zooming the image
    """
    # Error management
    if not isinstance(image_data, np.ndarray):
        raise ValueError("image_data (1st argument) must be a NumPy array")
    elif not isinstance(scale, (int, float)) or scale <= 0:
        raise ValueError("scale (2nd argument) must be a positive int/float")

    # Get height and width of image
    height, width = image_data.shape[0], image_data.shape[1]

    # Get new height and width based on scaling factor
    new_height, new_width = round(height // scale), round(width // scale)

    # Get starting index for both axis after zoom at middle
    start_h_index = round((height - new_height) / 2)
    start_w_index = round((width - new_width) / 2)

    # Slice initial image to new zoomed image
    zoomed_image = image_data[
        start_h_index:(start_h_index + new_height),
        start_w_index:(start_w_index + new_width)
    ]

    # Convert the image to grayscale (average of RGB channels) then reshape
    # the array to new shape
    grayscale = np.reshape(
        np.mean(zoomed_image, axis=2).astype(int),
        (new_height, new_width, 1)
    )

    # Print messages regarding grayscale image properties
    print(
        f"New shape after slicing: {grayscale.shape}"
        f" or {grayscale.shape[:2]}"
    )
    print(grayscale)

    # Matplotlib
    plt.imshow(grayscale, cmap="grey")
    plt.savefig('zoomed_image.png', bbox_inches='tight')
    # UserWarning: FigureCanvasAgg is non-interactive, and thus cannot be shown
    # plt.show()


def main():
    """Main function"""
    image_data = ft_load("animal.jpeg")
    scale = 2
    if image_data is not None:
        zoom_image(image_data, scale)


if __name__ == "__main__":
    import numpy as np
    import matplotlib.pyplot as plt
    from load_image import ft_load
    main()
