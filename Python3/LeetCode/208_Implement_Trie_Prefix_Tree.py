class TrieNode:
    def __init__(self):
        self.trinodes = [None] * 26
        self.terminating = False
    
    def _next(self, index):
        return self.trinodes[index]

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        
    def _charToIndex(self, c):
        return ord(c) - ord('a')

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        current = self.root
        for char in word:
            index = self._charToIndex(char)
            if None == current.trinodes[index]:
                current.trinodes[index] = TrieNode()
            current = current._next(index)
        current.terminating = True
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        current = self.root
        for char in word:
            index = self._charToIndex(char)
            if None == current.trinodes[index]:
                return False
            current = current._next(index)
        return current.terminating
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        current = self.root
        for char in prefix:
            index = self._charToIndex(char)
            if None == current.trinodes[index]:
                return False
            current = current._next(index)
        if current.terminating:
            return True
        for curr in current.trinodes:
            if None != curr:
                return True
        return False
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)