from functools import reduce
from typing import Dict


def count_occurrences(text: str) -> dict:
    """
    Returns a dictionary of occurances of every unique character present
    time: O(n)
    """
    count: dict = {}
    for char in text:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    return count


def count_occurrences_with_ignore(text: str, ignore_chars: str) -> dict:
    """
    Returns a dictionary of occurrences of every unique character present,
    excluding any present in the ignore_chars input

    args:
        text -- string input to be counted
        ignore_chars -- string contain all forbidden characters

    time: O(n)
    """
    count: Dict[str, int] = {}
    for char in text:
        if char in ignore_chars:
            continue
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    return count


def count_occurrences_with_reduce(test: str) -> dict:
    count_dict: dict = reduce(frequency_reducer, test, {})
    return count_dict


def frequency_reducer(count_dict: dict, character: str) -> dict:
    if character in count_dict:
        count_dict[character] += 1
    else:
        count_dict[character] = 1
    return count_dict


def count_occurrences_advanced(text: str, ignore_chars: str, sort_count=False) -> list:
    """Returns an orders list of tuples consisting of ("char", count)

    args:
        text -- string input to be counted
        ignore_chars -- string list of forbidden characters
        sorted_count -- (optional) if True, sorts the count in ascending order, False by default
    """
    count_dict: dict = {}
    for char in text:
        if char in ignore_chars:
            continue
        if char in count_dict:
            count_dict[char] += 1
        else:
            count_dict[char] = 1
    count_list = list(count_dict.items())
    if sort_count:
        count_list = sorted(count_list, key=lambda it: it[1])  # sort by count value
    return count_list
