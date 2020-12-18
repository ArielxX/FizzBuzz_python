import pytest
from main.FizzBuzz import get_FizzBuzz

def test_FizzBuzz():
	assert get_FizzBuzz(15) == "FizzBuzz"
	assert get_FizzBuzz(30) == "FizzBuzz"
	assert get_FizzBuzz(45) == "FizzBuzz"
	assert get_FizzBuzz(60) == "FizzBuzz"
	assert get_FizzBuzz(75) == "FizzBuzz"
	assert get_FizzBuzz(90) == "FizzBuzz"