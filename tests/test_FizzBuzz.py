from fizzbuzz.fizzbuzz import get_fizzbuzz


def test_fizzbuzz():
    # Testing cases with divisible by 15 numbers
    assert get_fizzbuzz(15) == "FizzBuzz"
    assert get_fizzbuzz(30) == "FizzBuzz"
    assert get_fizzbuzz(45) == "FizzBuzz"
    assert get_fizzbuzz(60) == "FizzBuzz"
    assert get_fizzbuzz(75) == "FizzBuzz"
    assert get_fizzbuzz(90) == "FizzBuzz"
