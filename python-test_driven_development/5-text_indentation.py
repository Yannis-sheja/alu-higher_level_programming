#!/usr/bin/python3
"""This module defines a function that indents text"""


def text_identation(text):
    """Prints a text with 2 new lines after '.', '?' and ':'
    Raise:
    TypeError: if text is not a string
    """

    if text is not str:
        raise TypeError("text must be a string")
    c = 0
    while c < len(text) and text[c] == ' ':
        c += 1

    while c < len(text):
        print(text[c], end="")
        if text[c] == "\n" or text[c] in ".?:":
            if text[c] in ".?:":
                print("\n")
            c += 1
            while c < len(text) and text[c] == ' ':
                c += 1
            continue
        c += 1
