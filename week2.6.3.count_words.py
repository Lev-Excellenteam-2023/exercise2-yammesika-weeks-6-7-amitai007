# region count words - this 2

def count_words(text):
    """
    Count the number of words in a text and their lengths.

    Args: text (str): The text to count words from.

    Returns:  dict: A dictionary where keys are words and values are their lengths.
    """
    # Clean the text
    cleaned_text = ''.join(c if c.isalpha() else ' ' for c in text)

    # Split the text
    words = cleaned_text.lower().split()

    # Create a dictionary
    word_lengths = {word: len(word) for word in words}

    return word_lengths
# endregion

def main():
    # Example
    text = "The quick brown fox jumps over the lazy dog."
    word_lengths = count_words(text)
    print("Word lengths:")
    for word, length in word_lengths.items():
        print(f"{word}: {length}")


if __name__ == "__main__":
    main()




