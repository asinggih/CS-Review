#!/usr/bin/env python3

"""
The major difference between a queue and a stack is the order of elements.
A queue removes the oldest item and a stack removes the newest item.
How could you remove the oldest item from a stack
if you only had access to the newest item?

We can remove the oldest item from a stack by repeatedly
removing the newest item (inserting those into the temporary stack)
until we get down to one element.
Then, after we've retrieved the newest item, putting all the elements back.
The issue with this is that doing several pops in a row
will require 0 (N) work each time.

Can we optimize for scenarios where we might do several pops in a row?
"""


from Stack import Stack


class MyQueue:

    def __init__(self):
        self.new_top = Stack()
        self.old_top = Stack()

    def add(self, item):
        """Adding item into the queue"""

        self.new_top.push(item)

    def _shift_stacks(self):
        """helper function to move item from new top to
        old top stacks"""

        # only shift when old_top is empty
        if self.old_top.is_empty() is True:
            while self.new_top.is_empty() is False:
                self.old_top.push(self.new_top.pop().value)

    def remove(self):
        """Removing item from the queue"""

        self._shift_stacks()
        return self.old_top.pop()

    def peek(self):
        """show the first one in queue"""

        self._shift_stacks()
        return self.old_top.peek()

    def is_empty(self):
        """check if the queue is empty"""

        if self.new_top.is_empty() and self.old_top.is_empty():
            return True
        return False
