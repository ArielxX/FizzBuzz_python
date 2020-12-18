from fizzbuzz.fizzbuzz import get_fizzbuzz

def test_end():
	# Testing cases with the last numbers
	assert get_fizzbuzz(90) == "FizzBuzz"
	assert get_fizzbuzz(91) == "91"
	assert get_fizzbuzz(92) == "92"
	assert get_fizzbuzz(93) == "Fizz"
	assert get_fizzbuzz(94) == "94"
	assert get_fizzbuzz(95) == "Buzz"
	assert get_fizzbuzz(96) == "Fizz"
	assert get_fizzbuzz(97) == "97"
	assert get_fizzbuzz(98) == "98"
	assert get_fizzbuzz(99) == "Fizz"
	assert get_fizzbuzz(100) == "Buzz"