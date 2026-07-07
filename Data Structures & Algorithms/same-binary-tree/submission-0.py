# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        result = True

        def dfs(p, q):
            nonlocal result

            if not p and not q:
                return

            if not p or not q or not result:
                result = False
                return

            if p.val != q.val:
                result = False

            dfs(p.left, q.left)
            dfs(p.right, q.right)

        dfs(p, q)
        return result

            