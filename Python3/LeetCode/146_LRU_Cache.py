class ListNode:
    def __init__(self, key = 0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.node_map = {}
        self.dummy_head = ListNode()
        self.dummy_tail = ListNode()
        self.dummy_head.next = self.dummy_tail
        self.dummy_tail.prev = self.dummy_head
        

    def get(self, key: int) -> int:
        if key in self.node_map:
            res = self.node_map[key]
            self.delete(self.node_map[key])
            self.add(res)
            return res.val
        return -1
    def put(self, key: int, value: int) -> None:
        if key in self.node_map:
            self.delete(self.node_map[key])
        new_node = ListNode(key,value)
        self.add(new_node)
        self.node_map[key] = new_node
        if len(self.node_map) > self.capacity:
            node = self.dummy_tail.prev
            self.delete(node)
            del self.node_map[node.key]
            
    
    def add(self, new_node):
        new_node.next = self.dummy_head.next
        new_node.prev = self.dummy_head
        self.dummy_head.next.prev = new_node
        self.dummy_head.next = new_node
        
    def delete(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
