"""Test cases are important."""


from fun import homework


def test_greatest_number():
    """Quick test to see if you can find the largest number in a list."""
    assert homework.find_greatest_number([1, 2, 3, 4, 5, 6, 7, 8]) == 8
    assert homework.find_greatest_number([7, 3, 21, 4, 1, 6]) == 21


def test_least_number():
    """Quick test to see if you can find the smallest number in a list."""
    assert homework.find_least_number([1, 2, 3, 4, 5, 6, 7, 8]) == 1
    assert homework.find_least_number([8, 7, 3, 2, 4, 1, 6]) == 1


def test_sum_of_list():
    """Quick test to see if you can add together all the numbers in a list."""
    assert homework.add_list_numbers([1, 2, 3, 4]) == 10
    assert homework.add_list_numbers([]) == 0
    assert homework.add_list_numbers(None) == 0


def test_key_with_the_longest_value():
    """A little trickier.   Which KEY has the 'longest' value associated with it? """

    assert (
        homework.longest_value_key({"dog": "cat", "a": "asdfasdfasdfasdfasdf"}) == "a"
    )
    assert homework.longest_value_key({}) is None
    assert homework.longest_value_key(None) is None
