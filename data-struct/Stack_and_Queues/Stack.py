#!/usr/bin/env python3

from Node import Node


class Stack:

    def __init__(self):
        self.top = None
        self.size = 0

    def is_empty(self):
        if self.top is None:
            return True

    def push(self, item):
        node = Node(item)
        if self.top is None:
            self.top = node
        else:   # if stack is not empty
            node.next = self.top
            self.top = node

        self.size += 1

    def pop(self):
        if self.top is None:
            raise AttributeError("EmptyStackError")
        to_be_popped = self.top
        self.top = to_be_popped.next

        self.size -= 1

        return to_be_popped

    def peek(self):
        return self.top
