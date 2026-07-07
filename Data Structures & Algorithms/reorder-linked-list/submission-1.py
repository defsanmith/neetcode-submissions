# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # split ll in two parts
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse l2
        second = slow.next
        prev = slow.next = None
        while second:
            nextNode = second.next
            second.next = prev
            prev = second
            second = nextNode

        # merge l1 and l2
        l1, l2 = head, prev
        while l2:
            t1 = l1.next
            t2 = l2.next
            l1.next = l2
            l2.next = t1
            l1 = t1
            l2 = t2