"""
Fixed Window Counter
How it works:

Divide time into fixed windows (e.g. every 60 seconds)
Count requests in the current window
If count exceeds limit → reject
When window expires → reset counter to 0

"""

from threading import Lock
import time
from rate_limiter import RateLimiter

class FixedWindowCounter(RateLimiter):
    def __init__(self, limit, window_size):
        self.limit = limit
        self.window_size = window_size
        self.count = 0
        self.window_start = time.time()
        self.lock = Lock()

    def _reset_window(self):
        # TODO: check if current window has expired
        # if yes: reset count to 0, update window_start
        curr_time = time.time()
        if curr_time - self.window_start >= self.window_size:
            self.count = 0
            self.window_start = curr_time

    def acquire(self):
        with self.lock:
            # TODO: reset if expired, then check count against limit
            self._reset_window()
            if self.count < self.limit:
                self.count += 1
                return True
            
            return False

def main():
    fw = FixedWindowCounter(limit=3, window_size=2.0)  # 3 requests per 2 seconds

    for i in range(10):
        allowed = fw.acquire()
        print(f"Request {i+1}: {'✅ allowed' if allowed else '❌ rejected'}")
        time.sleep(0.5)

if __name__ == '__main__':
    main()