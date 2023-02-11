import time
from katas.add import add


def test_add() -> None:
    acceptable_time_in_seconds = 0.3
    nr_samples = 1_000_000
    start_time = time.time()
    add(1, 1)
    assert time.time() - start_time < acceptable_time_in_seconds
