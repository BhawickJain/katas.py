from katas.queue import Queue


def test_queue__initialise() -> None:
    queue_list = Queue[int]()
    assert queue_list._items == []


def test_queue__enqueue() -> None:
    queue_list = Queue[int]()
    queue_list.enqueue(5)
    queue_list.enqueue(1)
    assert queue_list._items == [5, 1]


def test_queue__dequeue() -> None:
    queue_list = Queue[int]()
    queue_list.enqueue(5)
    queue_list.enqueue(1)
    item = queue_list.dequeue()
    assert item == 5
    assert queue_list._items == [1]


def test_queue__dequeue_object() -> None:
    queue_list = Queue[object]()
    queue_list.enqueue({"rating": 50})
    queue_list.enqueue({"rating": 20})
    item = queue_list.dequeue()
    assert item == {"rating": 50}
    assert queue_list._items == [{"rating": 20}]
