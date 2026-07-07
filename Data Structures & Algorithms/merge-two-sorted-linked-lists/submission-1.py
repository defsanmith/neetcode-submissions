# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # define dummy node
        dummy = node = ListNode()

        # while list1 and list2
        while list1 and list2:
            # if list1.val < list2.val
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            # move the node to next pointer
            node = node.next

        # add remaining nodes
        node.next = list1 or list2

        # return dummy.next
        return dummy.next