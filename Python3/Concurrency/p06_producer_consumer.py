"""
Problem 6 of 10 — "Producer-Consumer with a Queue"
This is one of the most common concurrency patterns in interviews — and in real systems like Kafka consumers.
Scenario: One producer thread generates 10 items and puts them on a queue. Two consumer threads pull items off and process them. Use queue.Queue — it's thread-safe by design, no Lock needed.
"""

from threading import Thread
from queue import Queue
import time

def producer(q):
    for i in range(10):
        print(f"Produced item {i}")
        q.put(i)
        time.sleep(0.1)
    for _ in range(2):
        q.put(None)
    # TODO: send a stop signal for each consumer

def consumer(q, name):
    while True:
        item = q.get()
        # TODO: check for stop signal and break
        if item is None:
            q.task_done()
            break
        print(f"{name} consumed {item}")
        q.task_done()

def main():
    q = Queue()
    consumers = [Thread(target=consumer, args=[q, f"C{i}"]) for i in range(2)]
    prod = Thread(target=producer, args=[q])

    for c in consumers: c.start()
    prod.start()

    prod.join()
    q.join()  # blocks until every q.put() has a matching q.task_done()

if __name__ == '__main__':
    main()