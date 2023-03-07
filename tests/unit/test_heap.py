from katas.heap import heap


def test_heap__initialisation():
    hp = heap()
    assert hp.store == []


def test_heap__insert_values_1():
    hp = heap()
    hp.insert(10)
    assert hp.store == [10]
    hp.insert(5)
    assert hp.store == [10, 5]
    hp.insert(6)
    assert hp.store == [10, 5, 6]
    hp.insert(1)
    assert hp.store == [10, 5, 6, 1]
    hp.insert(2)
    assert hp.store == [10, 5, 6, 1, 2]
    hp.insert(11)
    assert hp.store == [11, 5, 10, 1, 2, 6]
    hp.insert(12)
    assert hp.store == [12, 5, 11, 1, 2, 6, 10]


def test_heap__returns_correct_order_1():
    hp = heap()
    hp.insert(10)
    hp.insert(5)
    hp.insert(6)
    hp.insert(1)
    hp.insert(2)
    hp.insert(11)
    hp.insert(12)
    assert hp.remove() == 12
    assert hp.remove() == 11
    assert hp.remove() == 10
    assert hp.remove() == 6
    assert hp.remove() == 5
    assert hp.remove() == 2
    assert hp.remove() == 1


def test_heap__insert_values_2():
    hp = heap()
    hp.insert(10)
    hp.insert(20)
    hp.insert(30)
    hp.insert(45)
    hp.insert(11)
    hp.insert(6)
    hp.insert(10)
    assert hp.store == [45, 30, 20, 10, 11, 6, 10]


def test_heap__returns_correct_order_2():
    hp = heap()
    hp.insert(6)
    hp.insert(10)
    hp.insert(1)
    hp.insert(5)
    hp.insert(2)
    hp.insert(11)
    hp.insert(20)
    hp.insert(10)
    hp.insert(30)
    hp.insert(45)
    assert hp.remove() == 45
    assert hp.remove() == 30
    assert hp.remove() == 20
    assert hp.remove() == 11
    assert hp.remove() == 10
    assert hp.remove() == 10
    assert hp.remove() == 6
    assert hp.remove() == 5
    assert hp.remove() == 2
    assert hp.remove() == 1


def test_heap__find_parent_of_6():
    assert heap.get_parent(5) == 2
    assert heap.get_parent(6) == 2


def test_heap__find_parent_of_0():
    assert heap.get_parent(0) == None


def test_heap__find_parent_of_1():
    assert heap.get_parent(1) == 0
