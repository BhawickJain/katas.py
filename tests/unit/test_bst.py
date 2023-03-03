from katas.bst import Bst


def test_Bst__initialise_class() -> None:
    bst = Bst(5)
    assert bst.root_node.value == 5


def test_Bst__insert_lower_value() -> None:
    bst = Bst(5)
    bst.insert(4)
    assert bst.root_node.low.value == 4


def test_Bst__insert_higher_value() -> None:
    bst = Bst(5)
    bst.insert(10)
    assert bst.root_node.high.value == 10


def test_Bst__insert_equal_value() -> None:
    bst = Bst(5)
    bst.insert(5)
    assert bst.root_node.low.value == 5


def test_Bst__insert_equal_value() -> None:
    bst = Bst(5)
    bst.insert(6)
    bst.insert(7)
    bst.insert(8)
    assert bst.root_node.high.high.high.value == 8


def test_Bst__find_a_value() -> None:
    bst = Bst(5)
    bst.insert(6)
    bst.insert(7)
    bst.insert(8)
    found = bst.find(8)
    assert found == True


def test_Bst__find_a_value_does_not_exist() -> None:
    bst = Bst(5)
    bst.insert(6)
    bst.insert(7)
    bst.insert(8)
    found = bst.find(10)
    assert found == False
