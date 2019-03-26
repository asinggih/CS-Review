#!/usr/bin/env python3

"""
Given a circular linked list, implement an algorithm that returns the node
at the beginning of the loop.

EXAMPLE
Input: A -> B -> C -> 0 -> E -> C [the same C as earlier]
Output: C

"""


def detect_loop(head):
    """detecting if a linked list is a vicious circle """

    seen = set()

    current_node = head
    while current_node.next is not None:
        if current_node in seen:
            return current_node
        seen.add(current_node)
        current_node = current_node.next
    return None
