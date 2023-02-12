from typing import Union, Generic, TypeVar
"""Binary Search Tree"""

T = TypeVar("T")

class Bst(Generic[T]):
    def __init__(self, root_value: int):
        self.root_node = Node(root_value)
    def insert(self, value):
        current_node = self.root_node
        while True:
            if value <= current_node.value:
                if current_node.low != None:
                   current_node = current_node.low
                   continue
                else:
                    current_node.low = Node(value)
                    break
            if value > current_node.value:
                if current_node.high != None:
                    current_node = current_node.high
                    continue
                else:
                    current_node.high= Node(value)
                    break
            return True
    def find(self, value):
        current_node = self.root_node
        while current_node is not None:
            if current_node.value == value:
                return True
            if value <= current_node.value:
                current_node = current_node.low
                continue
            else:
                current_node = current_node.high
                continue
        return False

    def auto_balance(self):
        # bredth first tree travesal into a list of values (time: O(n))
        # sort using a O(nLog(n)) algorithm like merge sort
        # compute midian index of sorted list
        # create new BST with median
        # add values from median index to 0
        # add values from medan index to end
        # ! not inplace
        pass


class Node(Generic[T]):
    def __init__(self, value):
        self.value: T = value
        self.low: Union[Node, None] = None
        self.high: Union[Node, None] = None

    def __repr__(self) -> str:
        return repr({"value": self.value, "low": self.low, "high": self.high})
    