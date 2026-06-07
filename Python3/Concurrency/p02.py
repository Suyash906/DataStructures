"""    
Problem 2 of 10 — "Thread with a loop"
Write a function count_up(name, n) that prints "{name}: {i}" for each i from 1 to n inclusive. Spawn 3 threads with args ("A", 3), ("B", 3), ("C", 3) — all running concurrently. Wait for all three to finish.
Expected output (order will vary each run — that's intentional):
"""
import threading

def count_up(name, n):
    for i in range(1, n + 1):
        print(f'{name}:{i}')

def main2():
    
    tasks = [("A", 3), ("B", 3), ("C", 3)]
    
    threads = []
    
    for name, count in tasks:
        thread = threading.Thread(target=count_up, args=[name, count])
        thread.start()
        threads.append(thread)
    
    for thread in threads:
        thread.join()