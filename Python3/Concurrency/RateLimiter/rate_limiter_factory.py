from rate_limiter import RateLimiter
from fixed_window import FixedWindowCounter
from sliding_window_log import SlidingWindowLog
from token_bucket import TokenBucket


class RateLimiterFactory:
    @staticmethod
    def create(algorithm: str, **kwargs) -> RateLimiter:
        algorithms = {
            "token_bucket": TokenBucket,
            "fixed_window": FixedWindowCounter,
            "sliding_window_log": SlidingWindowLog,
        }
        if algorithm not in algorithms:
            raise ValueError(f"Unknown algorithm: '{algorithm}'. Choose from: {list(algorithms.keys())}")
        return algorithms[algorithm](**kwargs)
    
limiter = RateLimiterFactory.create("token_bucket", refill_rate=2, capacity=5)
limiter.acquire()

limiter2 = RateLimiterFactory.create("fixed_window", limit=3, window_size=2.0)
limiter2.acquire()