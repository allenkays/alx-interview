#!/usr/bin/env python3
"""Module UTF-8 Validation"""


def validUTF8(data):
    """method that determines if a given data set
    represents a valid UTF-8 encoding"""

    try:
        bytes(data).decode("UTF-8")
        return True
    except UnicodeDecodeError:
        return False
