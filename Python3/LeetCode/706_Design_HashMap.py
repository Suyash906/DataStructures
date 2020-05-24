class HashNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hashmap = [None for i in range(16)] 
        

    def getHashCode(self, key):
        return key % 16
    
    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        hashcode = self.getHashCode(key)
        if None == self.hashmap[hashcode]:
            self.hashmap[hashcode] = HashNode(key, value)
        else:
            p = self.hashmap[hashcode]
            if p.next is None:
                if p.key == key:
                    p.value = value
                else:
                    p.next = HashNode(key, value)
                return
            while p.next is not None:
                if p.key == key:
                    p.value = value
                    return
                p = p.next
            if p.key == key:
                p.value = value
            else:
                p.next = HashNode(key, value)

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        hashcode = self.getHashCode(key)
        if self.hashmap[hashcode] is None:
            return -1
        p = self.hashmap[hashcode]
        while p is not None:
            if p.key == key:
                return p.value
            p = p.next
        return -1
         

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        hashcode = self.getHashCode(key)
        if self.hashmap[hashcode] is not None:
            p = self.hashmap[hashcode]
            if p.key == key:
                if p.next is None:
                    self.hashmap[hashcode] = None
                else:
                    self.hashmap[hashcode] = p.next
                return
            else:
                while p.next is not None:
                    if p.next.key == key:
                        p.next = p.next.next
                        return
                    p = p.next
                        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
