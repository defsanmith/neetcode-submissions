"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old_to_copy = { None: None}

        current = head
        while current:
            old_to_copy[current] = Node(current.val)
            current = current.next

        current = head
        while current:
            new_node = old_to_copy[current]
            new_node.next = old_to_copy[current.next]
            new_node.random = old_to_copy[current.random]
            current = current.next

        return old_to_copy[head] 