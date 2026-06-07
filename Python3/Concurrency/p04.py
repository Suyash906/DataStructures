"""
Problem 4 of 10 — "Worker that waits for a signal"
This introduces threading.Event — used when one thread needs to wait for another thread to signal it's ready.
Scenario: You have a worker thread that should not start processing until the main thread finishes some setup. Use threading.Event to coordinate this.
"""

from threading import Thread, Event
import time

def worker(event, name):
    print(f"{name} waiting for signal...")
    # TODO: block here until event is set
    event.wait()
    print(f"{name} got signal, starting work!")
    time.sleep(0.5)
    print(f"{name} done.")

def main():
    event = Event()
    
    threads = [Thread(target=worker, args=[event, f"W{i}"]) for i in range(3)]
    for t in threads: t.start()
    
    print("Main: doing setup...")
    time.sleep(1)  # simulate setup work
    print("Main: setup done, signaling workers!")
    # TODO: fire the signal here
    event.set()
    
    for t in threads: t.join()

if __name__ == '__main__':
    main()