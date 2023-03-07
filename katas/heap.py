from typing import Generic, TypeVar, Tuple
import math

T = TypeVar("T")


class heap:
    def __init__(self):
        self.store = []

    def insert(self, value: int) -> None:
        self.store.append(value)
        value_idx = len(self.store) - 1
        parent_idx = heap.get_parent(value_idx)
        swapped = True
        while swapped & isinstance(parent_idx, int):
            if self.store[value_idx] < self.store[parent_idx]:
                swapped = False
            else:
                self.swap_positions(value_idx, parent_idx)
                value_idx = parent_idx
                parent_idx = self.get_parent(value_idx)
                swapped = True

    def remove(self) -> int | None:
        if len(self.store) == 0:
            return None
        if len(self.store) == 1:
            return self.store.pop()

        last_item = self.store.pop()
        removed_item = self.store[0]
        self.store[0] = last_item
        last_item_position = 0
        swapped = True
        while swapped:
            largest_child_idx = self.get_largest_child_idx(last_item_position)
            print(largest_child_idx)
            if (
                isinstance(largest_child_idx, int) & self.store[last_item_position]
                < largest_child_idx
            ):
                self.swap_positions(largest_child_idx, last_item_position)
                last_item_position = largest_child_idx
                swapped = True
            else:
                swapped = False
        return removed_item

    def swap_positions(self, position_a: int, position_b: int) -> Tuple[int, int]:
        position_a_value = self.store[position_a]
        self.store[position_a] = self.store[position_b]
        self.store[position_b] = position_a_value
        return (position_b, position_a)

    def get_largest_child_idx(self, last_item_position: int) -> int | None:
        left_child_idx = self.get_child_left(last_item_position)
        right_child_idx = self.get_child_right(last_item_position)
        if left_child_idx > len(self.store) & right_child_idx > len(self.store):
            return None
        if left_child_idx > len(self.store) & right_child_idx < len(self.store):
            return right_child_idx
        if right_child_idx > len(self.store) & left_child_idx < len(self.store):
            return left_child_idx
        if self.store[left_child_idx] > self.store[right_child_idx]:
            return left_child_idx
        else:
            return right_child_idx

    @staticmethod
    def get_parent(child_index: int) -> int | None:
        parent_idx = math.floor((child_index + 1) / 2) - 1
        if parent_idx < 0:
            return None
        return parent_idx

    @staticmethod
    def get_child_left(parent_idx: int) -> int:
        return 2 * (parent_idx + 1) - 1

    @staticmethod
    def get_child_right(parent_idx: int) -> int:
        return 2 * (parent_idx + 1)
