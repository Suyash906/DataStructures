"""
Problem statement:
Implement a RateLimitedExecutor that runs tasks concurrently but enforces two constraints:

Max 3 tasks running concurrently at any time
Tasks are processed in the order they were submitted — results must be printed in submission order, not completion order

Your class should support:
"""

import time, random
from threading import Semaphore
from concurrent.futures import ThreadPoolExecutor

class RateLimiterExecutor():
    def __init__(self, max_concurrent=3):
        self.max_concurrent = max_concurrent
        self.sem = Semaphore(max_concurrent)
        self.task_ids = []

    def submit(self, task_id):
        self.task_ids.append(task_id)

    def run(self):
        with ThreadPoolExecutor(max_workers=self.max_concurrent) as executor:
            futures = [executor.submit(run_task, self.sem, id) for id in self.task_ids]

            for future in futures:
                result = future.result()
                print(result)



def run_task(sem, task_id):
    with sem:
        return process_video(task_id)


def process_video(task_id):
    duration = random.uniform(0.5, 1.5)
    time.sleep(duration)
    return f"Video {task_id} processed in {duration:.2f}s"



