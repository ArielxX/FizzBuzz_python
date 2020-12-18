import pytest
from main.FizzBuzz import get_FizzBuzz

def test_end():
	assert get_FizzBuzz(90) == "FizzBuzz"
	assert get_FizzBuzz(91) == "91"
	assert get_FizzBuzz(92) == "92"
	assert get_FizzBuzz(93) == "Fizz"
	assert get_FizzBuzz(94) == "94"
	assert get_FizzBuzz(95) == "Buzz"
	assert get_FizzBuzz(96) == "Fizz"
	assert get_FizzBuzz(97) == "97"
	assert get_FizzBuzz(98) == "98"
	assert get_FizzBuzz(99) == "Fizz"
	assert get_FizzBuzz(100) == "Buzz"