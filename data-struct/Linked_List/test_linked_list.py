#!/usr/bin/env python3

from Node import Node


def test_node_creation_with_value():
    """Testing node object creation with a value"""

    test_node = Node(12)
    assert test_node.value == 12


def test_node_creation_with_default_value():
    """Testing node object creation without giving any values"""

    test_node = Node()
    assert test_node.value is None


def test_setting_next_node():
    """setting 'next' value of current node"""

    current_node = Node(12)
    next_node = Node(40)
    current_node.next = next_node

    assert current_node.next.value == 40
