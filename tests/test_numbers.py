import pytest
from main.FizzBuzz import get_FizzBuzz

def test_numbers():
	assert get_FizzBuzz(1) == "1"
	assert get_FizzBuzz(2) == "2"
	assert get_FizzBuzz(8) == "8"
	assert get_FizzBuzz(16) == "16"
	assert get_FizzBuzz(31) == "31"
	assert get_FizzBuzz(43) == "43"
	assert get_FizzBuzz(58) == "58"
	assert get_FizzBuzz(62) == "62"
	assert get_FizzBuzz(64) == "64"
	assert get_FizzBuzz(88) == "88"
	assert get_FizzBuzz(97) == "97"