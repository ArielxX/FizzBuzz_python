# Testing cases with divisible by 3 and not by 5 numbers
from fizzbuzz.fizzbuzz import get_fizzbuzz


def test_Fizz():
    # Testing cases with divisible by 3 and not by 5 numbers
    assert get_fizzbuzz(3) == "Fizz"
    assert get_fizzbuzz(6) == "Fizz"
    assert get_fizzbuzz(9) == "Fizz"
    assert get_fizzbuzz(12) == "Fizz"
    assert get_fizzbuzz(21) == "Fizz"
    assert get_fizzbuzz(51) == "Fizz"
    assert get_fizzbuzz(84) == "Fizz"
    assert get_fizzbuzz(93) == "Fizz"
    assert get_fizzbuzz(99) == "Fizz"
