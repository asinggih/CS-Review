#!/usr/bin/env python3

from Node import Node
from MyLinkedList import MyLinkedList
import pytest


def test_removing_duplicates():
    """Test removing duplicates from linked list and check size"""

    L = [5, 10, 20, 30, 12, 10, 20, 56]
    ll = MyLinkedList()
    for i in L:
        ll.append(Node(i))
    ll.remove_dups()
    check = set(L)

    assert len(check) == ll.size

    ll = ll.display().split(", ")
    for i in ll:
        assert int(i) in check


def test_finding_kth_to_last_element():
    """test finding the kth to last element in linked list"""

    L = [1, 2, 3, 4, 5]
    ll = MyLinkedList()
    for i in L:
        ll.append(Node(i))

    assert ll.kth_to_last(3) == 2


def test_finding_kth_to_last_out_of_range():
    """test finding the kth to last element in linked list"""

    L = [1, 2, 3, 4, 5]
    ll = MyLinkedList()
    for i in L:
        ll.append(Node(i))

    with pytest.raises(IndexError) as e:
        ll.kth_to_last(5)
    assert str(
        e.value) == "0 < k < Linked List's size"
