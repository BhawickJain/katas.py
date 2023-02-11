from katas.collect_high import collect_high


def test_collect_high_with_iterator():
    expected_result = [1, 2, 3, 4]
    iterator = iter(expected_result)
    callback_fn = lambda: next(iterator)
    repeat = 4
    assert collect_high(callback_fn, repeat) == expected_result
