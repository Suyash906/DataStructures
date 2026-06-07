from threading import Lock
import time
from rate_limiter import RateLimiter


class TokenBucket(RateLimiter):
    def __init__(self, refill_rate:float, capacity:float):
        self.refill_rate = refill_rate
        self.capacity = capacity
        self.tokens = capacity
        self.last_refill = time.time()
        self.lock = Lock()

    
    def _refill(self):
        # TODO: calculate how many tokens to add based on
        # time elapsed since last refill
        # cap tokens at capacity
        # update last_refill timestamp
        curr_time = time.time()
        elapsed = curr_time - self.last_refill
        new_tokens = elapsed * self.refill_rate
        self.tokens = min(self.capacity, self.tokens + new_tokens)
        self.last_refill = curr_time
        

    def acquire(self):
        with self.lock:
            # TODO: refill first, then check if token available
            # if yes: consume one, return True
            # if no: return False
            self._refill()
            if self.tokens >= 1:
                self.tokens -= 1
                return True
            return False



def main():
    bucket = TokenBucket(refill_rate=1, capacity=5)  # 2 tokens/sec, max 5

    for i in range(8):
        allowed = bucket.acquire()
        print(f"Request {i+1}: {'✅ allowed' if allowed else '❌ rejected'}")
        time.sleep(0.3)

if __name__ == '__main__':
    main()
