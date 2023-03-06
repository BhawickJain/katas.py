from typing import Union, Generic, TypeVar, Optional

"""Binary Search Tree"""

T = TypeVar("T")


class Bst:
    def __init__(self, root_value: int) -> None:
        self.root_node: Node[int] = Node[int](root_value)

    def insert(self, value) -> None:
        current_node = self.root_node
        while True:
            if value <= current_node.value:
                # use isinstance to type narrow / type guard
                if isinstance(current_node.low, Node):
                    current_node = current_node.low
                    continue
                else:
                    current_node.low = Node(value)
                    break
            if value > current_node.value:
                if isinstance(current_node.high, Node):
                    current_node = current_node.high
                    continue
                else:
                    current_node.high = Node(value)
                    break

    def find(self, value: int) -> bool:
        current_node: Optional[Node] = self.root_node
        while isinstance(current_node, Node):
            if current_node.value == value:
                return True
            if value <= current_node.value:
                current_node = current_node.low
                continue
            else:
                current_node = current_node.high
                continue
        return False

    def auto_balance(self) -> None:
        # breadth first tree traversal into a list of values (time: O(n))
        # sort using a O(nLog(n)) algorithm like merge sort
        # compute midian index of sorted list
        # create new BST with median
        # add values from median index to 0
        # add values from medan index to end
        # ! not inplace
        pass


class Node(Generic[T]):
    def __init__(self, value) -> None:
        self.value: T = value
        self.low: Optional[Node] = None
        self.high: Optional[Node] = None

    def __repr__(self) -> str:
        return repr({"value": self.value, "low": self.low, "high": self.high})
