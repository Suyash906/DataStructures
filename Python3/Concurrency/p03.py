"""
Problem 3 of 10 — "Shared counter (broken)"
This is where it gets interesting.

Your task: Run this code. Observe that the output is less than 500_000 and changes every run. Then fix it using threading.Lock() so it always prints exactly 500_000.
Two things to submit:

The broken output you observed
Your fixed code using a lock
"""


from threading import Thread, Lock

counter = 0

def increment(lock):
    global counter
    for _ in range(1_000_000):
        with lock:
            counter += 1

lock = Lock()

threads = [Thread(target=increment, args=[lock]) for _ in range(5)]
for t in threads: t.start()
for t in threads: t.join()

print(counter)  # Expected: 500_000. What actually prints?