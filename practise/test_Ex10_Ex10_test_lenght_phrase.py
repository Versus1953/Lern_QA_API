import pytest

def test_phrase_length():
    phrase = input("Set a phrase: ")
    assert len(phrase) < 15, "phrase has to be no longer than 15 characters"