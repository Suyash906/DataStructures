class MinHeap:
	array = []
	count = 0
	capacity = 0
	def __init__(self, capacity):
		self.capacity = capacity

	def parent(self, i):
		if i <=0 and i >= self.count:
			return -1
		else:
			return (i-1) // 2

	def leftChild(self, i):
		left = (2 * i)+1
		if left > self.count:
			return -1
		return left

	def rightChild(self, i):
		right = (2*i) + 2
		if right>self.count:
			return -1
		return right

	def getMinimum(self):
		if self.count == 0:
			return -1
		else:
			return self.array[0]

	def percolateDown(self, i):
		l = left(i)
		r  = right(i)

		if -1 != l and self.array[l] < self.array[i]:
			small = l 
		else:
			small = i

		if -1 != r and self.array[r] < self.array[small]:
			small  = r

		if i != small: 
			temp = self.array[i]
			self.array[i] = self.array[small]
			self.array[small] = temp
			percolateDown(small)

	def deleteMin(self):
		if self.count == 0:
			return -1
		data = self.array[0]
		self.array[0] = self.array[self.count-1]
		self.count -= 1
		percolateDown(0)
		return data

	def resizeHeap(self):
		self.capacity *= 2

	def insert(self, data):
		if self.count == self.capacity:
			self.resizeHeap()

		self.count += 1
		i = self.count - 1

		while i>=0 and data < self.array[parent(i)]:
			self.array[parent(i)] = self.array[i]
			i = parent(i)

		self.array[i] = data

	def destroyHeap(self):
		self.count = 0
		self.array = []