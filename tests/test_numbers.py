from fizzbuzz.fizzbuzz import get_fizzbuzz

def test_numbers():
	# Testing cases with non divisible by 3 or 5 numbers
	assert get_fizzbuzz(1) == "1"
	assert get_fizzbuzz(2) == "2"
	assert get_fizzbuzz(8) == "8"
	assert get_fizzbuzz(16) == "16"
	assert get_fizzbuzz(31) == "31"
	assert get_fizzbuzz(43) == "43"
	assert get_fizzbuzz(58) == "58"
	assert get_fizzbuzz(62) == "62"
	assert get_fizzbuzz(64) == "64"
	assert get_fizzbuzz(88) == "88"
	assert get_fizzbuzz(97) == "97"