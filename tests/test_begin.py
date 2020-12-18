from fizzbuzz.fizzbuzz import get_fizzbuzz


def test_begin():
    # Testing cases with the first numbers
    assert get_fizzbuzz(1) == "1"
    assert get_fizzbuzz(2) == "2"
    assert get_fizzbuzz(3) == "Fizz"
    assert get_fizzbuzz(4) == "4"
    assert get_fizzbuzz(5) == "Buzz"
    assert get_fizzbuzz(6) == "Fizz"
    assert get_fizzbuzz(7) == "7"
    assert get_fizzbuzz(8) == "8"
    assert get_fizzbuzz(9) == "Fizz"
    assert get_fizzbuzz(10) == "Buzz"
