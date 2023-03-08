from typing import Generic, TypeVar, Tuple
import math

T = TypeVar("T")

class heap:
    def __init__(self):
        self.store = []

    def insert(self, value: int) -> None:
        self.store.append(value)
        value_idx = len(self.store) - 1
        self.bubble_up(value_idx)

    def bubble_up(self, target_idx: int) -> None:
        parent_idx = heap.get_parent(target_idx)
        swapped = True
        while swapped:
            if parent_idx is None:
                swapped = False
                break
            if self.store[target_idx] < self.store[parent_idx]:
                swapped = False
            else:
                self.swap_positions(target_idx, parent_idx)
                target_idx = parent_idx
                parent_idx = self.get_parent(target_idx)
                swapped = True

    def sink_down(self, target_idx: int) -> None:
        swapped = True
        while swapped:
            largest_child_idx = self.get_largest_child_idx(target_idx)
            print("largest_child", largest_child_idx)
            if not isinstance(largest_child_idx, int):
                swapped = False
            elif self.store[target_idx] < self.store[largest_child_idx]:
                self.swap_positions(largest_child_idx, target_idx)
                target_idx = largest_child_idx
                swapped = True
            else:
                swapped = False

    def remove(self) -> int | None:
        if len(self.store) == 0:
            return None
        if len(self.store) == 1:
            return self.store.pop()

        last_item = self.store.pop()
        removed_item = self.store[0]
        self.store[0] = last_item
        last_item_position = 0
        self.sink_down(last_item_position)
        return removed_item

    def swap_positions(self, position_a: int, position_b: int) -> Tuple[int, int]:
        position_a_value = self.store[position_a]
        self.store[position_a] = self.store[position_b]
        self.store[position_b] = position_a_value
        return (position_b, position_a)

    def get_largest_child_idx(self, last_item_position: int) -> int | None:
        left_child_idx = self.get_child_left(last_item_position)
        right_child_idx = self.get_child_right(last_item_position)
        max_index = len(self.store) - 1
        print(max_index, left_child_idx, right_child_idx)
        if left_child_idx > max_index and right_child_idx > max_index:
            return None
        elif left_child_idx > max_index:
            return right_child_idx
        elif right_child_idx > max_index:
            print("meh", right_child_idx > max_index, left_child_idx < max_index)
            return left_child_idx
        elif self.store[left_child_idx] > self.store[right_child_idx]:
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
