class PrefixTree:

    def __init__(self):
        self.children = [0] * 26
        self.is_end = False

    def get_index(self, c):
        return ord(c) - ord('a')

    def insert(self, word: str) -> None:
        node = self

        for c in word:
            index = self.get_index(c)
            if not node.children[index]:
                node.children[index] = PrefixTree()

            node = node.children[index]

        node.is_end = True


    def search(self, word: str) -> bool:
        node = self

        for c in word:
            index = self.get_index(c)
            if not node.children[index]:
                return False
            
            node = node.children[index]
        
        return node.is_end
        

    def startsWith(self, prefix: str) -> bool:
        node = self

        for c in prefix:
            index = self.get_index(c)
            if not node.children[index]:
                return False

            node = node.children[index]

        return True if node else False
        
        