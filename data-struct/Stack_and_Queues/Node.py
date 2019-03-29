#!/usr/bin/env python3


class Node:
    """Node class to be used with Linked List"""

    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next = next_node
