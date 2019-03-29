#!/usr/bin/env python3

import pytest
from Stack import Stack


def test_empty_stack_size():
    """Testing the size of the stack when nothing is pushed"""

    stack = Stack()
    assert stack.size == 0


def test_is_empty_function():
    """Testing the 'is empty' function of the stack"""

    stack = Stack()
    assert stack.is_empty() is True


def test_pushing_item_into_stack():
    """test adding items into the stack"""

    stack = Stack()

    x = "blob"
    stack.push(x)
    assert stack.top.value == "blob"
    assert stack.size == 1

    y = "hello"
    stack.push(y)
    assert stack.top.value == "hello"
    assert stack.size == 2


def test_popping_item_from_stack():
    """test popping item out of stack"""

    stack = Stack()

    x = "blob"
    stack.push(x)

    y = "hello"
    stack.push(y)

    assert stack.pop().value == "hello"
    assert stack.size == 1
    assert stack.pop().value == "blob"
    assert stack.size == 0


def test_popping_item_from_empty_stack():
    """test popping item from emtpy stack"""

    stack = Stack()

    with pytest.raises(AttributeError) as e:
        stack.pop()

    assert str(e.value) == "EmptyStackError"
