import pytest
from main.FizzBuzz import get_FizzBuzz

def test_begin():
	assert get_FizzBuzz(1) == "1"
	assert get_FizzBuzz(2) == "2"
	assert get_FizzBuzz(3) == "Fizz"
	assert get_FizzBuzz(4) == "4"
	assert get_FizzBuzz(5) == "Buzz"
	assert get_FizzBuzz(6) == "Fizz"
	assert get_FizzBuzz(7) == "7"
	assert get_FizzBuzz(8) == "8"
	assert get_FizzBuzz(9) == "Fizz"
	assert get_FizzBuzz(10) == "Buzz"