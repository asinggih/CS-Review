#!/usr/bin/env python3

from Queue import Queue
import pytest


def test_queue_initialisation():

    q = Queue()

    assert q._first is None
    assert q._last is None


def test_adding_item_into_queue():

    q = Queue()

    q.add("hello")
    assert q._first.value == "hello"
    assert q._last.value == "hello"

    q.add("blob")
    assert q._first.value == "hello"
    assert q._last.value == "blob"


def test_removing_item_from_the_queue():

    q = Queue()

    q.add("hello")
    q.add("blob")

    assert q.remove().value == "hello"
    assert q.remove().value == "blob"
    with pytest.raises(AttributeError) as e:
        q.remove()
    assert str(e.value) == "EmptyQueueError"


def test_peeking_the_queue():

    q = Queue()

    q.add("hello")
    q.add("blob")

    assert q.peek().value == "hello"


def test_empty_status_of_queue():

    q = Queue()

    assert q.is_empty() is True
