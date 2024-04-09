#!/usr/bin/python3
"""Module 5-text_indentation
Contains function 5-text_indentation(text) with prints
a text with 2 new lines after each of these characters: ., ? and :
"""


def text_indentation(text):
    """Prints a text with two new lines after ., ?, and : characters.

    Args:
        text (str): The text to be formatted (must be a string).

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for c in ".:?":
        text = text.replace(c, c + "\n\n")

    processed_text = "\n".join([line.strip() for line in text.split('\n')])
    print(processed_text, end='')
