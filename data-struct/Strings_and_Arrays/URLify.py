#!/usr/bin/env python3
#
# Written by asinggih 07/02/2019

"""
Write a method to replace all spaces in a string with '%20: You may assume
that the string has sufficient space at the end to hold the additional
characters, and that you are given the "true" length of the string.
(Note: If implementing in Java, please use a character array so that you can
perform this operation in place.)

EXAMPLE

    Input: "Mr John Smith       ", 13
    Output: "Mr%20John%20Smith"

"""


def general(string_input, true_length):
    """URLifying a string by replacing whitespaces with %20"""
    out_container = []
    for i in range(true_length):
        if string_input[i] == " ":
            out_container.append("%20")
        else:
            out_container.append(string_input[i])

    return "".join(out_container)


def pythonic(string_input, true_length):
    """URLifying a string by replacing whitespaces with %20"""
    stripped = string_input.strip()
    out = stripped.replace(" ", "%20")
    print(out)


if __name__ == "__main__":
    x = "  Mr John Smith       "
    y = 13
    pythonic(x, y)
