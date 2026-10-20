# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return 'N'
            
        result = []

        q = deque([root])
        while q:
            q_len = len(q)
            for _ in range(q_len):
                node = q.popleft()
                
                result.append(str(node.val if node else 'N'))
                
                if node:
                    q.append(node.left)
                    q.append(node.right)
                    
        return ','.join(result)


        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        data = data.split(',')
        if data[0] == 'N':
            return None

        root = TreeNode(data[0])
        q = deque([root])
        i = 1

        while q:
            q_len = len(q)

            for _ in range(q_len):
                node = q.popleft()

                if data[i] != 'N':
                    node.left = TreeNode(data[i])
                    q.append(node.left)
                i += 1
                
                if data[i] != 'N':
                    node.right = TreeNode(data[i])
                    q.append(node.right)
                i += 1

        return root
