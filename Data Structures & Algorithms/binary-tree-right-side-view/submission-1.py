from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        q = deque()
        q.append(root)

        while q:
            qLength = len(q)
            rightSide = None
            for _ in range(qLength):
                node = q.popleft()
                if node:
                    rightSide = node
                    q.append(node.left)
                    q.append(node.right)
                
            if rightSide:
                result.append(rightSide.val)

        return result