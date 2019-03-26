#!/usr/bin/env python3

from Node import Node
from LinkedList import LinkedList

from loop_detection import detect_loop
from palindrome import palindrome


def test_loop_detection():
    """test if a linked list is a circular linked list"""

    A = Node("A")
    B = Node("B")
    C = Node("C")
    D = Node("D")
    E = Node("E")

    A.next = B
    B.next = C
    C.next = D
    D.next = E
    E.next = C

    assert detect_loop(A) == C


def test_loop_detection_no_loop():
    """test if a linked list is a circular linked list"""

    A = Node("A")
    B = Node("B")
    C = Node("C")
    D = Node("D")
    E = Node("E")

    A.next = B
    B.next = C
    C.next = D
    D.next = E

    assert detect_loop(A) is None


def test_if_linked_list_is_palindrome():
    """testing if linked list is a palindrome"""

    L = [1, 2, 3, 2, 1]

    ll = LinkedList()
    for i in L:
        ll.append(Node(i))

    assert palindrome(ll) is True


def test_if_linked_list_is_palindrome_wrong_input():
    """testing if linked list is a palindrome"""

    L = [1, 4, 5, 3, 2, 1]

    ll = LinkedList()
    for i in L:
        ll.append(Node(i))

    assert palindrome(ll) is False
