from katas.first_item import first


def test_first__handles_number_list() -> None:
    # create test input
    input_sequence = [1, 2, 3, 4]
    assert first(input_sequence) == 1


def test_first__handles_string_list() -> None:
    # create test input
    input_sequence = ["a", "b", "c", "d"]
    assert first(input_sequence) == "a"


def test_first__handles_object_list() -> None:
    # create test input
    input_sequence = [{"a": 1}, {"b": 1}, {"c": 1}, {"d": 1}]
    assert first(input_sequence) == {"a": 1}
