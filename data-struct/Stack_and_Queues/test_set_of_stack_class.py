#!/usr/bin/env python3

import pytest
from Stack_Of_Stacks import SetOfStacks


def test_sos_initialisation():
    """Testing set of stacks initialisation"""

    sos = SetOfStacks(5)
    assert sos.limit == 5
    assert sos.container == []
    assert sos.current is None


def test_sos_initialisation_too_low_threshold():
    """Testing set of stacks initialisation when threshold <= 1"""

    with pytest.raises(ValueError) as e:
        SetOfStacks(1)

    assert str(e.value) == "Just use a normal stack"


def test_pushing_item_into_sos():
    """test adding items into the set of stacks"""

    sos = SetOfStacks(2)

    a = 1
    sos.push(a)

    b = 2
    sos.push(b)

    assert sos.current == sos.container[0]

    c = 3
    sos.push(c)
    assert sos.current == sos.container[1]

    d = 4
    sos.push(d)

    e = 5
    sos.push(e)
    assert sos.current == sos.container[2]


def test_popping_from_sos():
    """test popping from set of stacks"""

    sos = SetOfStacks(3)

    test_data = [1, 2, 3, 4]

    for i in test_data:
        sos.push(i)

    assert sos.pop().value == 4
    assert sos.current == sos.container[0]

    for _ in range(3):
        sos.pop()

    with pytest.raises(AttributeError) as e:
        sos.pop()
    assert str(e.value) == "EmptySetOfStacksError"


def test_popping_at_index():
    """test popping at a specific substack"""

    sos = SetOfStacks(2)

    test_data = [1, 2, 3, 4]

    for i in test_data:
        sos.push(i)

    with pytest.raises(IndexError) as e:
        sos.pop_at(len(test_data))
    assert str(e.value) == "IndexOutOfRange"

    assert sos.pop_at(0).value == 2

    for _ in range(3):
        sos.pop()

    with pytest.raises(AttributeError) as e:
        sos.pop()
    assert str(e.value) == "EmptySetOfStacksError"
