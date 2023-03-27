# region count words - this 2

def count_words(text):
    # Clean the text by removing all non-alphabetic characters and replacing them with spaces
    cleaned_text = ''.join(c if c.isalpha() else ' ' for c in text)

    # Split the text into words and convert them to lowercase
    words = cleaned_text.lower().split()

    # Create a dictionary where the keys are the words and the values are their lengths
    # Duplicate words will be overwritten by the last occurrence of the word
    word_lengths = {word: len(word) for word in words}

    return word_lengths


# endregion
