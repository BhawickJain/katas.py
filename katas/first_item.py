from typing import TypeVar, Sequence

"""
Write a function `first_item` that takes a list of any type and returns the first item
"""

T = TypeVar("T")


def first(seq: Sequence[T]) -> T:
    return seq[0]
