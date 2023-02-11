from katas.random_gen import RandomGen, is_accurate_enough
import pytest


def test_validation__empty_probabilities() -> None:
    # Create empty probabilities and populated random_nums
    probabilities = []
    random_nums = [1, 2]

    # Catch expected error raised
    with pytest.raises(Exception) as exception_info:
        random_gen = RandomGen(random_nums, probabilities)

    # Check correct error message thrown
    assert str(exception_info.value) == "received empty list in one or more arguments"


def test_validation__random_nums() -> None:
    # Create empty random_nums and populated probabilities
    random_nums = []
    probabilities = [0.5]

    # Catch expected error raised
    with pytest.raises(Exception) as exception_info:
        random_gen = RandomGen(random_nums, probabilities)

    # Check correct error message thrown
    assert str(exception_info.value) == "received empty list in one or more arguments"


def test_validation__input_array_lengths_not_matching() -> None:
    # Create valid probabilities and random_nums inputs
    random_nums = [1, 2]
    probabilities = [0.5, 0.25, 0.25]

    # Catch expected error raised
    with pytest.raises(Exception) as exception_info:
        random_gen = RandomGen(random_nums, probabilities)

    # Check correct error message thrown
    assert (
        str(exception_info.value)
        == "length of number list does not match probability list"
    )


def test_validation__random_nums_contains_nonnumber_characters() -> None:
    # Create random_nums with a string item and valid probabilities
    random_nums = [1, 2, "3"]
    probabilities = [0.5, 0.25, 0.25]

    # Catch expected error raised
    with pytest.raises(Exception) as exception_info:
        random_gen = RandomGen(random_nums, probabilities)

    # Check correct error message thrown
    assert (
        str(exception_info.value)
        == "random_nums has non-numeric items, only numeric items expected"
    )


def test_validation__probabilities_contains_nonnumber_characters() -> None:
    # Create random_nums with a string item and valid probabilities
    random_nums = [1, 2, 3]
    probabilities = [0.5, "0.25", 0.25]

    # Catch expected error raised
    with pytest.raises(Exception) as exception_info:
        random_gen = RandomGen(random_nums, probabilities)

    # Check correct error message thrown
    assert (
        str(exception_info.value)
        == "probabilities has non-numeric items, only numeric items expected"
    )


def test_next_num__given_a_non_random_generator() -> None:
    # Create valid probabilities and random_nums inputs
    probabilities = [0.1, 0.2, 0.3, 0.4]
    random_nums = [1, 2, 3, 4]

    # Create a non-random generator between 0,1
    non_random = iter([0.1, 0.15, 0.35, 0.45, 0.67, 0.7833729496695886])

    def non_random_generator() -> float:
        return next(non_random)

    expected_next_random_nums = [1, 2, 3, 3, 4, 4]
    random_gen = RandomGen(random_nums, probabilities, non_random_generator)

    for i in range(5):
        # Check if correct next number chosen given random number value
        assert random_gen.next_num() == expected_next_random_nums[i]


def test_get_cumulative__from_valid_probability_array() -> None:
    # Create a valid probability array
    input = [0.1, 0.2, 0.3, 0.4]

    expected_result = [0.1, 0.3, 0.6, 1]
    result = RandomGen.get_cumulative(input)

    for idx in range(len(input)):
        # Check all values match expected result within given accuracy
        assert is_accurate_enough(result[idx], expected_result[idx], 0.001)


def test_validation_get_cumulative__when_probability_array_has_negative_numbers() -> (
    None
):
    # Create probability array with a negative number
    input = [-0.1, 0.4, 0.6]

    # Catch expected error raised
    with pytest.raises(Exception) as exception_info:
        RandomGen.get_cumulative(input)

    # Check correct error message thrown
    assert (
        str(exception_info.value) == "probability array input contains negative numbers"
    )


def test_validation_get_cumulative__when_frequency_does_not_add_up_to_1() -> None:
    # Create probability array that adds up to more than 1
    probabilities = [0.5, 0.6]

    # Catch expected error raised
    with pytest.raises(Exception) as exception_info:
        RandomGen.get_cumulative(probabilities)

    # Check correct error message thrown
    assert str(exception_info.value) == "probabilities do not cumulatively add to 1"


def test_find_index_ceiling() -> None:
    # Create valid cumulative array and a random number between 0,1
    input_cumulative = [0.1, 0.3, 0.6, 1]
    input_random_number = 0.0856

    expected_index = 0

    assert (
        # Check the correct index is found
        RandomGen.find_index_ceiling(input_random_number, input_cumulative)
        == expected_index
    )
