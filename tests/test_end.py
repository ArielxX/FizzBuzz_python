from fizzbuzz.fizzbuzz import get_fizzbuzz


def test_end():
    # Testing cases with the last numbers
    assert get_fizzbuzz(90)[0] == "FizzBuzz"
    assert get_fizzbuzz(91)[0] == "91"
    assert get_fizzbuzz(92)[0] == "92"
    assert get_fizzbuzz(93)[0] == "Fizz"
    assert get_fizzbuzz(94)[0] == "94"
    assert get_fizzbuzz(95)[0] == "Buzz"
    assert get_fizzbuzz(96)[0] == "Fizz"
    assert get_fizzbuzz(97)[0] == "97"
    assert get_fizzbuzz(98)[0] == "98"
    assert get_fizzbuzz(99)[0] == "Fizz"
    assert get_fizzbuzz(100)[0] == "Buzz"
