from katas.two_sum import two_sum

def test_two_sum__find_9() -> None:
    input_nums = [2,7,11,15]
    input_target = 9
    expected_result = (0,1)
    assert two_sum(input_nums, input_target) == expected_result

def test_two_sum__none_present() -> None:
    input_nums = [3,2,4]
    input_target = 6
    expected_result = (1,2)
    assert two_sum(input_nums, input_target) == expected_result

def test_two_sum__find_6() -> None:
    input_nums = [3,3]
    input_target = 6
    expected_result = (0,1)
    assert two_sum(input_nums, input_target) == expected_result