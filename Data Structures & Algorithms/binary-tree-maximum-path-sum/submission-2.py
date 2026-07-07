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

            currentSum = node.val + leftSum + rightSum

            result = max(result, currentSum)

            return max(node.val + max(leftSum, rightSum), 0)
        
        dfs(root)

        return result