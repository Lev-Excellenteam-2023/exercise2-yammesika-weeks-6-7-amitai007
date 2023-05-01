from PIL import Image

# region remember - this 2

def decode_message(path):
    """
    Decode a message hidden in a black and white image.

    Args: path (str): The file path to the image.

    Returns: str: The decoded message.
    """
    # Read
    img = Image.open(path)

    width, height = img.size

    # Find the row number where the black pixel is located in each column
    message_chars = [chr(row) for col in range(width) for row in range(height) if img.getpixel((col, row)) == (0, 0, 0)]

    # Concatenate the characters to form the message
    message = "".join(message_chars)

    return message

# endregion

def main():
    # Example
    path = "image.png"
    message = decode_message(path)
    print(f"Decoded message: {message}")


if __name__ == "__main__":
    main()
