class TrieNode:
    def __init__(self):
        self.terminating = 0
        self.triNodes = [None] * 26
    
    def next(self, index ):
        return self.triNodes[index]

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def _charToIndex(self, char):
        return ord(char) - ord('a')

    def query(self, input : str) -> int:
        current = self.root
        for char in input:
            index = self._charToIndex(char)
            if None == current.triNodes[index]:
                return 0
            current = current.next(index)
        return current.terminating
    
    def insert(self, input: str):
        current  = self.root
        for char in input:
            index = self._charToIndex(char)
            if None == current.triNodes[index]:
                current.triNodes[index] = TrieNode()
            current = current.next(index)
        current.terminating = current.terminating + 1
    
    def delete(self, input):
        current = self.root
        for char in input:
            index = self._charToIndex(char)
            if None == current.triNodes[index]:
                return
            current = current.next(index)
        current.terminating -= 1

    def update(self, oldVal, newVal):
        self.delete(oldVal)
        self.insert(newVal)


if __name__=='__main__':
    setOfStrings = ["pqrs", "pprt", "psst", "qqrs", "pqrs"]
    trie = Trie()
    for string in setOfStrings:
        trie.insert(string)
    print(trie.query('psst'))
    print(trie.query('pqrs'))
    trie.update('psst', 'qqrs')
    print(trie.query('qqrs'))
    print(trie.query('psst'))
