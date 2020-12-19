from fizzbuzz.fizzbuzz import get_fizzbuzz


def test_numbers():
    # Testing cases with non divisible by 3 or 5 numbers
    assert get_fizzbuzz(1)[0] == "1"
    assert get_fizzbuzz(2)[0] == "2"
    assert get_fizzbuzz(8)[0] == "8"
    assert get_fizzbuzz(16)[0] == "16"
    assert get_fizzbuzz(31)[0] == "31"
    assert get_fizzbuzz(43)[0] == "43"
    assert get_fizzbuzz(58)[0] == "58"
    assert get_fizzbuzz(62)[0] == "62"
    assert get_fizzbuzz(64)[0] == "64"
    assert get_fizzbuzz(88)[0] == "88"
    assert get_fizzbuzz(97)[0] == "97"
