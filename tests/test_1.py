import pytest
from main.FizzBuzz import get_FizzBuzz

def test1():
	assert get_FizzBuzz(3) == "Fizz"
	assert get_FizzBuzz(5) == "Buzz"
	assert get_FizzBuzz(11) == "11"
	assert get_FizzBuzz(15) == "FizzBuzz"