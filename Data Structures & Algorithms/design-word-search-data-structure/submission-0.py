class Trie:
    def __init__(self):
        self.children = [None] * 26
        self.is_end = False

    def insert(self, word):
        node = self

        for c in word:
            index = ord(c) - ord('a')
            if not node.children[index]:
                node.children[index] = Trie()
            
            node = node.children[index]
        
        node.is_end = True

class WordDictionary:

    def __init__(self):
        self.root = Trie()

    def addWord(self, word: str) -> None:
        self.root.insert(word)
        

    def search(self, word: str) -> bool:
        def dfs(j, root):
            node = root

            for i in range(j, len(word)):
                c = word[i]
                index = ord(c) - ord('a')

                if c == '.':
                    for child in node.children:
                        if child and dfs(i + 1, child):
                            return True

                    return False

                else:
                    if not node.children[index]:
                        return False
                    
                    node = node.children[index]
                
            return node.is_end

        return dfs(0, self.root)
