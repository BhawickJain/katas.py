from katas.digit_root import digit_root


def test_digit_root_of_16() -> None:
    input_number = 16
    expected_result = 7

    assert digit_root(input_number) == expected_result


def test_digit_root_of_942() -> None:
    input_number = 942
    expected_result = 6

    assert digit_root(input_number) == expected_result


def test_digit_root_of_132189() -> None:
    input_number = 132189
    expected_result = 6

    assert digit_root(input_number) == expected_result


def test_digit_root_of_493193() -> None:
    input_number = 493193
    expected_result = 2

    assert digit_root(input_number) == expected_result
