from katas.count_occurrences import (
    count_occurrences,
    count_occurrences_with_ignore,
    count_occurrences_with_reduce,
    count_occurrences_advanced,
)


def test_count_frequency_1() -> None:
    # create test input and expected result
    text = "hello"
    expected_result = {"h": 1, "e": 1, "l": 2, "o": 1}

    # check against expected result
    assert count_occurrences(text) == expected_result


def test_count_frequency_except_ignored_chars_1() -> None:
    # create test input and expected result
    text = "hello!"
    forbidden = " !"
    expected_result = {"h": 1, "e": 1, "l": 2, "o": 1}

    # check against expected result
    assert count_occurrences_with_ignore(text, forbidden) == expected_result


def test_count_frequency_with_reduce() -> None:
    # create test input and expected result
    text = "hello!"
    expected_result = {"h": 1, "e": 1, "l": 2, "o": 1, "!": 1}

    # check against expected result
    assert count_occurrences_with_reduce(text) == expected_result


def test_count_frequency_advanced() -> None:
    # create test input and expected result
    text = "hello!"
    forbidden = " !"
    expected_result = [("h", 1), ("e", 1), ("o", 1), ("l", 2)]

    # check against expected result
    assert (
        count_occurrences_advanced(text, forbidden, sort_count=True) == expected_result
    )
