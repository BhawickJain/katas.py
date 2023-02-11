from katas.herons_root import herons_root
import logging

LOGGER = logging.getLogger(__name__)


def test_returns_a_result():
    result = herons_root(25, 0.8)
    assert result != None


tests = [{"name": "", "square": 25, "accuracy": 0.5}]


def test_returns_root_of_25():
    square = 25
    accuracy = 0.5
    solver = herons_root(square, accuracy)
    result = solver.solve()
    LOGGER.debug(f"result: {result}")
    accurate_enough = (result > square - accuracy) or (result < square + accuracy)
    assert accurate_enough


def test_returns_root_of_4():
    square = 4
    accuracy = 0.005
    solver = herons_root(square, accuracy)
    result = solver.solve()
    print(result)
    accurate_enough = (result > square - accuracy) or (result < square + accuracy)
    assert accurate_enough


def test_returns_root_of_49():
    square = 49
    accuracy = 0.001
    solver = herons_root(square, accuracy)
    result = solver.solve()
    print(result)
    accurate_enough = (result > square - accuracy) or (result < square + accuracy)
    assert accurate_enough
