import pytest

phrase = input("Set a phrase: ")
class TestCheck:
    def test_check(self):
        expected_symbols = 16
        print(len(phrase))
        assert len(phrase) < expected_symbols, f"Длина фразы более 15 символов"
