#!/usr/bin/env python3

"""
Write a program to sort a stack such that the smallest items are on the
top. You can use an additional temporary stack, but you may not copy the
elements into any other data structure (such as an array).
The stack supports the following operations: push, pop, peek, and isEmpty.
"""

from Stack import Stack


def sorted_stack(stack):

    buffer_stack = Stack()

    if stack.is_empty() is False:
        buffer_stack.push(stack.pop().value)

    while stack.is_empty() is False:

        if stack.peek().value > buffer_stack.peek().value:
            current_largest = stack.pop()
            count = 0

            while buffer_stack.is_empty() is False and \
                    buffer_stack.peek().value <= current_largest.value:

                stack.push(buffer_stack.pop().value)
                count += 1

            buffer_stack.push(current_largest.value)

            for _ in range(count):
                buffer_stack.push(stack.pop().value)
        else:
            buffer_stack.push(stack.pop().value)

    return buffer_stack
