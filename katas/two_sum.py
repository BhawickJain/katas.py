from typing import List, Tuple, Dict

"""
Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution,
and you may not use the same element twice.

You can return the answer in any order.
"""


def two_sum(num_list: List[int], target: int) -> List[int]:
    """Return a tuple of two index positions to a given list item that add up to a target value
    if none found, (-1, -1) is returned

    args:
        num_list -- given list to find two index positions from that add up to target
        target -- the target integer the sum will add up to
    """
    complement = lambda value: target - value

    # save first index of value to avoid re-searches
    index_memo: Dict[int, int] = {}

    # for each integer, find its complement to sum to target
    for idx, val in enumerate(num_list):
        val_comp = complement(val)
        if not val_comp in index_memo:
            # find the index of complement by going through the num_list
            comp_idx = find_index(num_list, val_comp)
            index_memo[val_comp] = comp_idx
        if not val in index_memo:
            index_memo[val] = idx
        # if an index is found, stop and return the index pair
        if (index_memo[val_comp] != -1) and index_memo[val_comp] != idx:
            return sorted((index_memo[val_comp], idx))
    return [-1, -1]


def find_index(num_list: List[int], value: int) -> int:
    for idx, item in enumerate(num_list):
        if item == value:
            return idx
    return -1
