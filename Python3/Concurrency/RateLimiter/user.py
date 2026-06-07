from dataclasses import dataclass
from rate_limiter_factory import RateLimiterFactory

PLAN_CONFIG = {
    "free": {"algorithm": "fixed_window", "limit": 5, "window_size": 60.0},
    "pro": {"algorithm": "token_bucket", "refill_rate": 10, "capacity": 20},
    "enterprise": {"algorithm": "sliding_window_log", "limit": 100, "window_size": 60.0}
}

class User:
    def __init__(self, user_id: str, plan: str):
        self.user_id = user_id
        self.plan = plan
        self.rate_limiter = RateLimiterFactory.create(**PLAN_CONFIG[self.plan])

    def make_request(self, endpoint):
        if self.rate_limiter.acquire():
            print(f'allowerd user_id:{self.user_id} endpoint:{endpoint}')
        else:
            print(f'rejected user_id:{self.user_id} endpoint:{endpoint}')