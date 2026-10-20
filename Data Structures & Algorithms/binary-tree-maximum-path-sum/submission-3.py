# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        result = float('-inf')

        def dfs(node):
            nonlocal result
            
            if not node:
                return 0

            leftSum = dfs(node.left)
            rightSum = dfs(node.right)

            result = max(result, node.val + leftSum + rightSum)

            return max(max(0, node.val + leftSum), max(0, node.val + rightSum))

        dfs(root)
        return result