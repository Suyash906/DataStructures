"""
Sliding Window Log
How it works:

Keep a log of timestamps of recent requests
On each acquire(), evict timestamps older than window_size
If remaining timestamps < limit → allow, log current timestamp
No fixed boundaries — window slides with time
"""
from collections import deque
from threading import Lock
import time
from rate_limiter import RateLimiter

class SlidingWindowLog(RateLimiter):
    def __init__(self, limit, window_size):
        self.limit = limit
        self.window_size = window_size
        self.log = deque()
        self.lock = Lock()
        
    def _evict_expired(self, curr_time):
        # TODO: remove timestamps from the left of deque
        # that are older than (now - window_size)
        while self.log and self.log[0] < curr_time - self.window_size:
            _ = self.log.popleft()


    def acquire(self):
        with self.lock:
            curr_time = time.time()
            self._evict_expired(curr_time)
            if len(self.log) < self.limit:
                self.log.append(curr_time)
                return True
            return False

def main():
    sw = SlidingWindowLog(limit=3, window_size=2.0)

    for i in range(10):
        allowed = sw.acquire()
        print(f"Request {i+1}: {'✅ allowed' if allowed else '❌ rejected'}")
        time.sleep(0.5)

if __name__ == '__main__':
    main()