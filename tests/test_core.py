"""Unit tests for randalf.core."""

import random

from randalf import core


def test_alphabet_to_list_dedupes_and_sorts():
    assert core._alphabet_to_list("cbaabc") == ["a", "b", "c"]


def test_ranges_to_list_expands_digit_range():
    assert core._ranges_to_list("0-9") == list("0123456789")


def test_ranges_to_list_supports_multiple_ranges():
    # chr() is iterated 0..255, so ASCII order: digits before letters.
    assert core._ranges_to_list("a-f0-3") == list("0123abcdef")


def test_list_to_string_length_and_membership():
    alphabet = ["a", "b", "c"]
    result = core.list_to_string(alphabet, 20)
    assert len(result) == 20
    assert set(result) <= set(alphabet)


def test_list_to_string_zero_length_is_empty():
    assert core.list_to_string(["a"], 0) == ""


def test_generation_is_deterministic_under_seed():
    random.seed(1234)
    first = core.ranges_to_string("a-z", 32)
    random.seed(1234)
    second = core.ranges_to_string("a-z", 32)
    assert first == second


def test_alphabet_to_string_only_uses_given_chars():
    result = core.alphabet_to_string("0123456789abcdef", 50)
    assert len(result) == 50
    assert all(c in "0123456789abcdef" for c in result)
