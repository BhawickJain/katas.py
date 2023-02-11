from typing import TypeVar, List
from collections.abc import Callable

"""
A high-order function that takes a callback function, and a repetion count, and returns an array of results from the callback for each repetition
"""

T = TypeVar("T")


def collect_high(callback_fn: Callable[..., T], repeat: int) -> List[T]:
    """Returns an array of results from a given callback function and number of repeat calls.

    args:
        callback_fn -- Callable function with no input arguments
        repeat -- Number of calls to make, also length of the returned results array
    """
    collected_results: List[T] = []
    for it in range(repeat):
        collected_results.append(callback_fn())
    return collected_results
