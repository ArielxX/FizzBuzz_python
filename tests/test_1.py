from fizzbuzz.fizzbuzz import get_fizzbuzz

def test1():
	# Testing simple cases
	assert get_fizzbuzz(3) == "Fizz"
	assert get_fizzbuzz(5) == "Buzz"
	assert get_fizzbuzz(11) == "11"
	assert get_fizzbuzz(15) == "FizzBuzz"