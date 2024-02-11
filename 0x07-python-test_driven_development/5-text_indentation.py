#!/usr/bin/python3

"""

This module defines a function that prints 2 new lines after "." "?" and ":"

"""


def text_indentation(text):
    """Prints 2 new lines after ".", "?" and ":"
    Raises:
        TypeError: if text is not a string"""

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    text = text.strip(" ")
    new_text = ""
    i = 0
    while i < len(text):
        new_text += text[i]
        if text[i] in ['.', '?', ':'] or text[i] == '\n':
            if text[i] in ['.', '?', ':']:
                new_text += "\n\n"
            i += 1
            while i < len(text) and text[i] == " ":
                i += 1
            continue
        i += 1
    print(new_text, end="")
