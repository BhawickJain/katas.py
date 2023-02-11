from typing import Generic, TypeVar, List

T = TypeVar("T")


class Stack(Generic[T]):
    def __init__(self) -> None:
        # create stack with an empty list of type T
        self._items: List[T] = []

    def __repr__(self) -> str:
        return repr({"length": len(self._items)})

    def push(self, item: T) -> None:
        self._items.append(item)

    def pop(self) -> T:
        return self._items.pop()

    def is_empty(self) -> bool:
        return not self._items
