# region remember - this 2
from PIL import Image


def decode_message(path):
    # Read the image from file
    img = Image.open(path)

    # Get the width and height of the image
    width, height = img.size

    # Iterate over each column of the image
    message = ""
    for x in range(width):
        # Find the row number where the black pixel is located
        for y in range(height):
            pixel = img.getpixel((x, y))
            if pixel == (0, 0, 0):  # black pixel found
                # Convert the row number to its corresponding character
                char = chr(y)
                message += char
                break  # move to next column

    return message


# endregion