# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        half, fast = head, head.next

        while fast and fast.next:
            half = half.next
            fast = fast.next.next

        second = half.next
        prev = half.next = None
        while second:
            next = second.next
            second.next = prev
            prev = second
            second = next

        first, second = head, prev
        while second:
            next_1, next_2 = first.next, second.next
            first.next = second
            second.next = next_1
            first, second = next_1, next_2

