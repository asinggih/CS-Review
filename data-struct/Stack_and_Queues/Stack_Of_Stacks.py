#!/usr/bin/env python3

from Stack import Stack


class SetOfStacks:

    def __init__(self, limit):

        if limit <= 1:
            raise ValueError("Just use a normal stack")

        self.limit = limit
        self.container = []
        self.current = None

    def push(self, item):
        """function to push item into stack"""

        stack = self.current

        if stack is None or stack.size >= self.limit:
            new_stack = Stack()
            new_stack.push(item)
            self.current = new_stack
            self.container.append(new_stack)

        else:
            stack.push(item)

    def pop(self):
        """function to pop item from stack"""

        if self.container == []:
            raise AttributeError("EmptySetOfStacksError")

        out = self.current.pop()

        if self.current.is_empty():
            self.container.pop()  # remove the empty stack from the container
            if self.container != []:
                self.current = self.container[len(self.container)-1]
            else:
                self.current = None

        return out

    def pop_at(self, index):
        """function to pop at specific substack"""

        if index < 0 or index > len(self.container) - 1:
            raise IndexError("IndexOutOfRange")

        stack_to_be_popped = self.container[index]

        out = stack_to_be_popped.pop()

        if stack_to_be_popped.is_empty():
            # remove the empty stack from our container will be
            # O(n) since the empty stack can be in the middle
            # of the set of stacks
            self.container.remove(stack_to_be_popped)
            if self.container != []:
                self.current = self.container[len(self.container)-1]
            else:
                self.current = None

        return out
