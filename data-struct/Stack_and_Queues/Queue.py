#!/usr/bin/env python3

from Node import Node


class Queue:

    def __init__(self):
        self._first = None
        self._last = None

    # add
    def add(self, item):
        """Adding item into the queue"""

        node = Node(item)

        if self._last is not None:
            self._last.next = node

        self._last = node

        if self._first is None:
            self._first = self._last

    # remove
    def remove(self):
        """Removing item from the queue"""

        if self._first is None:
            raise AttributeError("EmptyQueueError")

        to_be_removed = self._first
        self._first = to_be_removed.next

        return to_be_removed

    # peek
    def peek(self):
        """show the first one in queue"""

        return self._first

    # is_empty
    def is_empty(self):
        """check if the queue is empty"""

        return self._first is None
