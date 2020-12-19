from fizzbuzz.fizzbuzz import get_fizzbuzz


def test1():
    # Testing simple cases
    assert get_fizzbuzz(3)[0] == "Fizz"
    assert get_fizzbuzz(5)[0] == "Buzz"
    assert get_fizzbuzz(11)[0] == "11"
    assert get_fizzbuzz(15)[0] == "FizzBuzz"
