from fizzbuzz.fizzbuzz import get_fizzbuzz


def test_Buzz():
    # Testing cases with divisible by 5 and not by 3 numbers
    assert get_fizzbuzz(5)[0] == "Buzz"
    assert get_fizzbuzz(10)[0] == "Buzz"
    assert get_fizzbuzz(20)[0] == "Buzz"
    assert get_fizzbuzz(25)[0] == "Buzz"
    assert get_fizzbuzz(35)[0] == "Buzz"
    assert get_fizzbuzz(40)[0] == "Buzz"
    assert get_fizzbuzz(70)[0] == "Buzz"
    assert get_fizzbuzz(80)[0] == "Buzz"
    assert get_fizzbuzz(100)[0] == "Buzz"
