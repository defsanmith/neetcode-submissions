# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def sameTree(self, r1, r2):
        if not r1 and not r2:
            return True

        if r1 and r2 and r1.val == r2.val:
            return self.sameTree(r1.left, r2.left) and self.sameTree(r1.right, r2.right)
        else:
            return False


    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        stack = [root]
        node = root
        while stack:
            node = stack.pop()
            if node and node.val == subRoot.val and self.sameTree(node, subRoot):
                return True
            if node:
                stack.append(node.left)
                stack.append(node.right)

        return False