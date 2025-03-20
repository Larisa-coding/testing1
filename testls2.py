import pytest
from mainls2 import count_vowels

def test_only_vowels():
    assert count_vowels("aeiou") == 5
    assert count_vowels("АЕЁИОУЫЭЮЯ") == 10

def test_no_vowels():
    assert count_vowels("bcdfghjklmnpqrstvwxyz") == 0
    assert count_vowels("1234567890!@#$%^&*()") == 0

def test_mixed_string():
    assert count_vowels("Hello, World!") == 3  # e, o, o
    assert count_vowels("Привет, мир!") == 3  # и, е, и
    assert count_vowels("PyThOn Is AwEsOmE!") == 7  # y, o, i, A, e, O, e
