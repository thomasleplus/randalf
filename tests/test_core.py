"""Unit tests for randalf.core."""

# Tests intentionally exercise private module helpers.
# pylint: disable=protected-access

import random

from randalf import core


def test_alphabet_to_list_dedupes_and_sorts():
    """An alphabet string is turned into a sorted list of unique characters."""
    assert core._alphabet_to_list("cbaabc") == ["a", "b", "c"]


def test_ranges_to_list_expands_digit_range():
    """A single range expands to every character it spans, inclusive."""
    assert core._ranges_to_list("0-9") == list("0123456789")


def test_ranges_to_list_supports_multiple_ranges():
    """Multiple ranges combine in ASCII order regardless of input order."""
    # chr() is iterated 0..255, so ASCII order: digits before letters.
    assert core._ranges_to_list("a-f0-3") == list("0123abcdef")


def test_list_to_string_length_and_membership():
    """The result has the requested length and only uses alphabet characters."""
    alphabet = ["a", "b", "c"]
    result = core.list_to_string(alphabet, 20)
    assert len(result) == 20
    assert set(result) <= set(alphabet)


def test_list_to_string_zero_length_is_empty():
    """A requested length of zero yields the empty string."""
    assert core.list_to_string(["a"], 0) == ""


def test_generation_is_deterministic_under_seed():
    """The same seed produces the same generated string."""
    random.seed(1234)
    first = core.ranges_to_string("a-z", 32)
    random.seed(1234)
    second = core.ranges_to_string("a-z", 32)
    assert first == second


def test_alphabet_to_string_only_uses_given_chars():
    """The result has the requested length and only uses the given characters."""
    result = core.alphabet_to_string("0123456789abcdef", 50)
    assert len(result) == 50
    assert all(c in "0123456789abcdef" for c in result)
