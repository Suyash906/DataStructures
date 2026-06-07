from abc import ABC, abstractmethod
class RateLimiter(ABC):
    @abstractmethod
    def acquire(self):
        pass