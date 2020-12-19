from fizzbuzz.fizzbuzz import get_fizzbuzz


def test_fizzbuzz():
    # Testing cases with divisible by 15 numbers
    assert get_fizzbuzz(15)[0] == "FizzBuzz"
    assert get_fizzbuzz(30)[0] == "FizzBuzz"
    assert get_fizzbuzz(45)[0] == "FizzBuzz"
    assert get_fizzbuzz(60)[0] == "FizzBuzz"
    assert get_fizzbuzz(75)[0] == "FizzBuzz"
    assert get_fizzbuzz(90)[0] == "FizzBuzz"
