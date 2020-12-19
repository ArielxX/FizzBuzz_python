from fizzbuzz.fizzbuzz import get_fizzbuzz


def test_begin():
    # Testing cases with the first numbers
    assert get_fizzbuzz(1)[0] == "1"
    assert get_fizzbuzz(2)[0] == "2"
    assert get_fizzbuzz(3)[0] == "Fizz"
    assert get_fizzbuzz(4)[0] == "4"
    assert get_fizzbuzz(5)[0] == "Buzz"
    assert get_fizzbuzz(6)[0] == "Fizz"
    assert get_fizzbuzz(7)[0] == "7"
    assert get_fizzbuzz(8)[0] == "8"
    assert get_fizzbuzz(9)[0] == "Fizz"
    assert get_fizzbuzz(10)[0] == "Buzz"
