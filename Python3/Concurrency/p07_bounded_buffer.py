"""
Problem 7 of 10 — "Bounded buffer with Condition"
Implement a BoundedBuffer class from scratch with capacity 3. One producer adds 8 items, one consumer removes 8 items. Producer waits when full, consumer waits when empty.
"""

from threading import Thread, Condition
import time

class BoundedBuffer:
    def __init__(self, capacity):
        self.buffer = []
        self.capacity = capacity
        self.cond = Condition()

    def put(self, item):
        with self.cond:
            while len(self.buffer) == self.capacity:
                self.cond.wait()
            self.buffer.append(item)
            print(f"Put {item} | buffer: {self.buffer}")
            self.cond.notify()  # TODO: notify a waiting consumer

    def get(self):
        with self.cond:
            while len(self.buffer) == 0:
                self.cond.wait()  # TODO: wait for an item
            item = self.buffer.pop(0)
            print(f"Got {item} | buffer: {self.buffer}")
            self.cond.notify()  # TODO: notify a waiting producer
            return item

def producer(bb):
    for i in range(8):
        bb.put(i)
        time.sleep(0.1)

def consumer(bb):
    for _ in range(8):
        bb.get()
        time.sleep(0.3)

if __name__ == '__main__':
    bb = BoundedBuffer(3)
    t1 = Thread(target=producer, args=[bb])
    t2 = Thread(target=consumer, args=[bb])
    t1.start()
    t2.start()
    t1.join()
    t2.join()