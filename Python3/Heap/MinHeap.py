class MinHeap:
    def __init__(self, array):
        self.heap = self.buildHeap(array)

    def buildHeap(self, array):
        self.heap = array
        n = len(array)
        for i in range((n//2)-1, -1, -1):
            self.siftDown(i)
        return self.heap
	
    def _parent(self, i):
        if i == 0: return -1
        return (i-1) // 2
    
    def _left(self, i):
        left_index = i * 2 + 1
        if left_index >= len(self.heap): return -1
        return left_index
	
    def _right(self, i):
        right_index = i * 2 + 2
        if right_index >= len(self.heap): return -1
        return right_index
	
    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def siftDown(self, i):
        left_child_index = self._left(i)
        min_index = i
        if -1 != left_child_index and self.heap[left_child_index] < self.heap[min_index]:
            min_index = left_child_index
        right_child_index = self._right(i)
        if -1 != right_child_index and self.heap[right_child_index] < self.heap[min_index]:
            min_index = right_child_index
        
        if min_index != i:
            self._swap(i, min_index)
            self.siftDown(min_index)
			
    def siftUp(self, i):
        parent_index = self._parent(i)
        if parent_index != -1:
            while parent_index != -1 and self.heap[parent_index] > self.heap[i]:
                self._swap(i, parent_index)
                i = parent_index
                parent_index = self._parent(i)

    def peek(self):
        return self.heap[0]

    def remove(self):
        res = self.heap[0]
        self._swap(0, len(self.heap)-1)
        self.heap.pop()
        self.siftDown(0)
        return res

    def insert(self, value):
        self.heap.append(value)
        self.siftUp(len(self.heap) - 1)
