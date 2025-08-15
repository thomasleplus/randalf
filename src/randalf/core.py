"""Randalf - Random String Generator
Generates a random string of a specified length using a given alphabet or ASCII ranges.
"""

import random
import re


def _alphabet_to_list(alphabet: str) -> list:
    """Converts an ASCII string into a character list."""
    return sorted(set(alphabet))


def _ranges_to_list(pattern: str) -> list:
    """Converts an ASCII range like '0-9A-F' into a character list."""
    chars = []
    regex = re.compile(f"^[{pattern}]$")
    for i in range(256):
        c = chr(i)
        if regex.match(c):
            chars.append(c)
    return chars


def list_to_string(alphabet: list, length: int) -> str:
    """Generates a random string of given length from the provided list of characters."""
    return "".join(random.choice(alphabet) for _ in range(length))


def alphabet_to_string(alphabet: str, length: int) -> str:
    """Generates a random string of given length from the characters in the provided string."""
    return list_to_string(_alphabet_to_list(alphabet), length)


def ranges_to_string(ranges: str, length: int) -> str:
    """Generates a random string of given length from the character ranges provided."""
    return list_to_string(_ranges_to_list(ranges), length)
