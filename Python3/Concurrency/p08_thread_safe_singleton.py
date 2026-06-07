"""
Problem 8 of 10 — "Thread-safe Singleton"
A classic OOP + concurrency combo that shows up at Netflix and similar companies.
Scenario: Implement a DatabaseConnection singleton — only one instance should ever be created, even if 10 threads try to instantiate it simultaneously.
"""

from threading import Thread, Lock

class DatabaseConnection:
    _instance = None
    _lock = Lock()

    @classmethod
    def get_instance(cls):
        # TODO: implement thread-safe singleton here
        # Hint: check _instance, acquire lock, check again, create if needed
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = cls()
        return cls._instance

    def query(self, sql):
        print(f"Executing: {sql}")

def worker(thread_id):
    db = DatabaseConnection.get_instance()
    print(f"Thread {thread_id} got instance id: {id(db)}")
    db.query(f"SELECT * FROM table_{thread_id}")

threads = [Thread(target=worker, args=[i]) for i in range(10)]
for t in threads: t.start()
for t in threads: t.join()

# All 10 lines should print the SAME instance id