# Testing cases with divisible by 3 and not by 5 numbers
from fizzbuzz.fizzbuzz import get_fizzbuzz


def test_Fizz():
    # Testing cases with divisible by 3 and not by 5 numbers
    assert get_fizzbuzz(3)[0] == "Fizz"
    assert get_fizzbuzz(6)[0] == "Fizz"
    assert get_fizzbuzz(9)[0] == "Fizz"
    assert get_fizzbuzz(12)[0] == "Fizz"
    assert get_fizzbuzz(21)[0] == "Fizz"
    assert get_fizzbuzz(51)[0] == "Fizz"
    assert get_fizzbuzz(84)[0] == "Fizz"
    assert get_fizzbuzz(93)[0] == "Fizz"
    assert get_fizzbuzz(99)[0] == "Fizz"
