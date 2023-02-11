from katas.stack import Stack
from typing import List


def test_stack__initialise() -> None:
    stack_items = Stack[int]()
    assert stack_items._items == []


def test_stack__push() -> None:
    stack_items = Stack[int]()
    stack_items.push(5)
    assert stack_items._items == [5]


def test_stack__pop() -> None:
    stack_items = Stack[int]()
    stack_items.push(5)
    stack_items.pop()
    assert stack_items._items == []


def test_stack__is_empty() -> None:
    stack_items = Stack[int]()
    stack_items.push(5)
    assert stack_items.is_empty() == False
    stack_items.pop()
    assert stack_items.is_empty() == True
