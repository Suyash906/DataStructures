"""
Problem 5 of 10 — "Semaphore as a rate limiter"
Scenario: You have 10 worker threads all trying to call an external API, but the API only allows 3 concurrent connections at a time. Use threading.Semaphore to enforce this limit.
"""

from threading import Thread, Semaphore
import time

def call_api(sem, worker_id):
    print(f"W{worker_id} waiting to connect...")
    # TODO: acquire semaphore here
    with sem:
        print(f"W{worker_id} connected")
        time.sleep(1)  # simulate API call
        print(f"W{worker_id} done, releasing")
        # TODO: release semaphore here

def main():
    sem = Semaphore(3)  # max 3 concurrent
    threads = [Thread(target=call_api, args=[sem, i]) for i in range(10)]
    for t in threads: t.start()
    for t in threads: t.join()

if __name__ == '__main__':
    main()