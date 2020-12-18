import pytest
from main.FizzBuzz import get_FizzBuzz

def test_Fizz():
	assert get_FizzBuzz(3) == "Fizz"
	assert get_FizzBuzz(6) == "Fizz"
	assert get_FizzBuzz(9) == "Fizz"
	assert get_FizzBuzz(12) == "Fizz"
	assert get_FizzBuzz(21) == "Fizz"
	assert get_FizzBuzz(51) == "Fizz"
	assert get_FizzBuzz(84) == "Fizz"
	assert get_FizzBuzz(93) == "Fizz"
	assert get_FizzBuzz(99) == "Fizz"