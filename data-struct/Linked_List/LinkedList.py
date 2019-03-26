#!/usr/bin/env python3


class LinkedList:

    def __init__(self, head=None):
        self.head = head
        if self.head is not None:
            self.size = 1
        else:
            self.size = 0

    def display(self):
        """quick way of checking what is inside the linked list"""
        out = []
        current_node = self.head
        while current_node is not None:
            out.append(str(current_node.value))
            current_node = current_node.next
        return (", ".join(out))

    def append(self, node):
        """appending node to the end of linked list"""

        if self.head is None:
            self.head = node
            self.size += 1
            return self.head

        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = node
        self.size += 1
        return self.head

    def delete(self, value):
        """deleting a node with a particular value"""

        current_node = self.head

        # if target value is at the head of the linked list
        if self.head.value == value:
            self.head = self.head.next
            self.size -= 1
            return self.head

        while current_node.next is not None:

            if current_node.next.value == value:
                temp = current_node.next
                current_node.next = current_node.next.next
                temp.next = None
                self.size -= 1
                return self.head    # returns straightaway once target is found

            current_node = current_node.next

            # if we are deleting the end of the linked list
            if current_node is None:
                return self.head

        return self.head

    def delete_at_index(self, index):
        """deleting a node at particular index"""

        if index > self.size - 1 or index < 0:
            raise IndexError(
                "Index has to be >= 0 and Index < than Linked List's size")

        current_node = self.head

        i = 0
        while i < index:
            current_node = current_node.next
            i += 1

        return self.delete(current_node.value)
