# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        first = head
        second = head

        while n > 0:
            first = first.next
            n -= 1

        if first == None:
            head = second.next
        else:
            prev = None
            while first:
                prev = second
                second = second.next
                first = first.next

            if prev == None:
                head = None
            else:
                prev.next = second.next

        return head