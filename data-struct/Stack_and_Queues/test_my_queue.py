#!/usr/bin/env python3

from My_Queue import MyQueue


def test_queue_init():
    """initialising new MyQueue object"""

    q = MyQueue()

    assert q.new_top.is_empty() is True
    assert q.old_top.is_empty() is True


def test_adding_item_to_queue():
    """test adding item into MyQueue"""

    q = MyQueue()

    for i in range(5):
        q.add(i)

    assert q.new_top.peek().value == 4


def test_removing_item_into_queue():
    """test removing item from MyQueue"""

    q = MyQueue()

    for i in range(5):
        q.add(i)

    assert q.remove().value == 0


def test_peeking_item_in_queue():
    """test removing item from MyQueue"""

    q = MyQueue()

    for i in range(5):
        q.add(i)

    assert q.peek().value == 0


def test_querying_empty_status():
    """test if queue is empty"""

    q = MyQueue()

    assert q.is_empty() is True

    for i in range(5):
        q.add(i)

    assert q.is_empty() is False
