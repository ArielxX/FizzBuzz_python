from fizzbuzz.fizzbuzz import get_fizzbuzz

def test_Buzz():
	# Testing cases with divisible by 5 and not by 3 numbers
	assert get_fizzbuzz(5) == "Buzz"
	assert get_fizzbuzz(10) == "Buzz"
	assert get_fizzbuzz(20) == "Buzz"
	assert get_fizzbuzz(25) == "Buzz"
	assert get_fizzbuzz(35) == "Buzz"
	assert get_fizzbuzz(40) == "Buzz"
	assert get_fizzbuzz(70) == "Buzz"
	assert get_fizzbuzz(80) == "Buzz"
	assert get_fizzbuzz(100) == "Buzz"