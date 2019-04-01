#!/usr/bin/env python3

from sort_stack import sorted_stack
from Stack import Stack


def test_stack_sorting():

    L = [3, 10, 24, 1, 0, 5, -20]

    stack = Stack()

    for i in L:
        stack.push(i)

    x = sorted_stack(stack)

    out = []
    while x.is_empty() is False:
        out.append(x.pop().value)

    assert out == sorted(L)
