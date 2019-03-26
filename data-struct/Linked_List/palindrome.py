#!/usr/bin/env python3

"""
Implement a function to check if a linked list is a palindrome.
"""


def palindrome(ll):

    stack = []

    current_node = ll.head
    partition = ll.size // 2

    for i in range(ll.size):

        if i < partition:
            stack.append(current_node.value)

        else:
            if ll.size % 2 == 0:
                if stack.pop() != current_node.value:
                    return False
            else:
                if i == partition:
                    current_node = current_node.next
                    continue

                if stack.pop() != current_node.value:
                    return False

        current_node = current_node.next

    return True
