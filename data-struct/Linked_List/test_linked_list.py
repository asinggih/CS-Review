#!/usr/bin/env python3

import pytest
from Node import Node
from LinkedList import LinkedList


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


def test_linked_list_creation():
    """Test initialisation of LinkedList object"""

    node = Node(12)
    node2 = Node(20)
    ll = LinkedList(node)
    ll.append(node2)

    assert ll.display() == "12, 20"


def test_linked_list_size_empty_head():

    ll = LinkedList()

    assert ll.size == 0


def test_linked_list_size_non_empty_head():

    ll = LinkedList(Node(20))
    ll.append(Node(30))

    assert ll.size == 2


def test_linked_list_append():

    ll = LinkedList()
    ll.append(Node(20))
    ll.append(Node(30))

    assert ll.display() == "20, 30"


def test_delete_value_middle():

    blob = [12, 30, 20, 43]
    ll = LinkedList()
    for i in blob:
        ll.append(Node(i))
    ll.delete(20)
    assert ll.display() == "12, 30, 43"


def test_delete_value_at_head():

    blob = [12, 30, 20, 43]
    ll = LinkedList()
    for i in blob:
        ll.append(Node(i))
    ll.delete(12)
    assert ll.display() == "30, 20, 43"


def test_delete_value_at_end():

    blob = [12, 30, 20, 43]
    ll = LinkedList()
    for i in blob:
        ll.append(Node(i))
    ll.delete(43)
    assert ll.display() == "12, 30, 20"


def test_delete_multiple():

    blob = [12, 30, 20, 43]
    ll = LinkedList()
    for i in blob:
        ll.append(Node(i))
    ll.delete(43)
    ll.delete(30)
    ll.delete(12)
    assert ll.display() == "20"


def test_delete_duplicates():

    blob = [12, 30, 43, 12, 50, 30]
    ll = LinkedList()
    for i in blob:
        ll.append(Node(i))
    ll.delete(30)
    assert "30" in ll.display()


def test_delete_at_index():

    blob = [12, 30, 43, 13, 50, 30]
    ll = LinkedList()
    for i in blob:
        ll.append(Node(i))
    ll.delete_at_index(0)
    print(ll.display())
    assert "12" not in ll.display()


def test_delete_at_index_out_of_range():
    ll = LinkedList(Node(20))
    with pytest.raises(IndexError) as e:
        # ll.delete_at_index(1)
        ll.delete_at_index(-1)
    assert str(
        e.value) == "Index has to be >= 0 and Index < than Linked List's size"
