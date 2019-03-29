#!/usr/bin/env python3


class Node:
    """Node class to be used with Stack"""

    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next = next_node
        self.substack_min = None
