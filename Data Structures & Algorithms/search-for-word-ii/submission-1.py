class Trie:
    def __init__(self):
        self.children = {}
        # self.end = False
        self.index = -1

    def insert(self, index, word):
        node = self

        for c in word:
            if c not in node.children:
                node.children[c] = Trie()

            node = node.children[c]
        
        # node.end = True
        node.index = index
            

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = Trie()

        for i, word in enumerate(words):
            root.insert(i, word)

        indices = []
        def dfs(x, y, node):
            c = board[x][y]
            board[x][y] = '*'

            if node.index >= 0:
                indices.append(node.index)
                node.index = -1

            directions = ((-1, 0), (0, 1), (1, 0), (0, -1))
            for dx, dy in directions:
                mx, ny = x + dx, y + dy

                if 0 <= mx < m and 0 <= ny < n and board[mx][ny] != '*' and board[mx][ny] in node.children:
                    dfs(mx, ny, node.children[board[mx][ny]])
            
            board[x][y] = c
            
        m, n = len(board), len(board[0])

        for x in range(m):
            for y in range(n):
                if board[x][y] in root.children:
                    dfs(x, y, root.children[board[x][y]])

        return [words[i] for i in indices]
        
        