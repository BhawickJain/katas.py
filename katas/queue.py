from typing import TypeVar, Generic, List, Union

T = TypeVar("T")

class Queue(Generic[T]):
    def __init__(self) -> None:
        self._items: List[T] = []

    def __repr__(self) -> str:
        return repr({"length": len(self._items)})

    def enqueue(self, item: T) -> None:
        """add an item to the queue"""
        self._items.append(item)

    def dequeue(self) -> Union[T, None]:
        """remove the first item in the list and return, returns None when queue is empty"""
        if len(self._items) == 0:
            return None
        first, *self._items = self._items
        return first
