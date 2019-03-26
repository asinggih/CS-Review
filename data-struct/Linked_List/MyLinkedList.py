#!/usr/bin/env python3

from LinkedList import LinkedList


class MyLinkedList(LinkedList):
    """includes methods from interview questions from \
    cracking the coding interview"""

    def remove_dups(self):
        """removing duplicates from linked list"""

        seen = set()
        current_node = self.head

        while current_node.next is not None:

            if current_node.value not in seen:
                seen.add(current_node.value)
            else:
                self.delete(current_node.value)

            current_node = current_node.next

        return self.head

    def kth_to_last(self, k):
        """finding the kth to last element of a singly linked list"""

        if k > self.size - 1 or k < 1:
            raise IndexError(
                "0 < k < Linked List's size")

        target = self.size - k
        current_node = self.head

        i = 0
        while i < target-1:
            current_node = current_node.next
            i += 1

        return current_node.value
