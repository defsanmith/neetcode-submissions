# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque([root])

        result = []

        while q:
            lQ = len(q)
            lastNode = None

            for _ in range(lQ):
                node = q.popleft()
                if node:
                    q.append(node.left)
                    q.append(node.right)
                    lastNode = node.val

            if lastNode:
                result.append(lastNode)

        return result
        