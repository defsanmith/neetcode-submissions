# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map = { n: i for i, n in enumerate(inorder) }
        
        self.pre_index = 0
        def dfs(l, r):
            if l > r:
                return None

            root_val = preorder[self.pre_index]
            self.pre_index += 1
            mid = inorder_map[root_val]
            node = TreeNode(root_val)
            node.left = dfs(l, mid - 1)
            node.right = dfs(mid + 1, r)

            return node
        
        return dfs(0, len(preorder) - 1)