import pytest
from main.FizzBuzz import get_FizzBuzz

def test_Buzz():
	assert get_FizzBuzz(5) == "Buzz"
	assert get_FizzBuzz(10) == "Buzz"
	assert get_FizzBuzz(20) == "Buzz"
	assert get_FizzBuzz(25) == "Buzz"
	assert get_FizzBuzz(35) == "Buzz"
	assert get_FizzBuzz(40) == "Buzz"
	assert get_FizzBuzz(70) == "Buzz"
	assert get_FizzBuzz(80) == "Buzz"
	assert get_FizzBuzz(100) == "Buzz"