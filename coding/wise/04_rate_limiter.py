"""
WISE PAIR PROGRAMMING — Problem 4: Rate Limiter

SCENARIO:
Wise API getting hammered. One client making 50K requests/min.
Limit each client to 100 requests per minute.
Over limit → 429 Too Many Requests.
"""

from dataclasses import dataclass
from datetime import datetime, timedelta


class TooManyRequestException(Exception):
    pass


class RateLimiter:
    def __init__(self, default_ttl=60, max_requests=100):
        self.default_ttl = timedelta(seconds=default_ttl)
        self.max_requests = max_requests
        self.store = {}

    def allow_request(self, key):
        """Check if request is allowed. If yes, increment counter."""
        now = datetime.now()
        entry = self.store.get(key)

        # First request from this client
        if not entry:
            self.store[key] = {"requests": 1, "window_start": now}
            return True

        # Window expired — reset counter, new window
        date_diff = now - entry["window_start"]
        if date_diff >= self.default_ttl:
            self.store[key] = {"requests": 1, "window_start": now}
            return True

        # Within window — check limit
        if entry["requests"] >= self.max_requests:
            return False

        # Under limit — allow and increment
        entry["requests"] += 1
        return True


@dataclass
class User:
    session: str
    ip: str
    client_id: str


class WiseApi:
    def __init__(self, rate_limiter=None):
        self.rate_limiter = rate_limiter or RateLimiter()

    def get_rate(self, user, rate):
        client_key = f"{user.session}_{user.ip}_{user.client_id}"
        if not self.rate_limiter.allow_request(client_key):
            raise TooManyRequestException("429 Too Many Requests")

        return self._request(rate)

    @staticmethod
    def _request(rate):
        fake_rates = {
            "GBP_USD": 1.27,
            "GBP_BRL": 6.35,
            "USD_BRL": 5.17,
            "USD_NGN": 1370.0,
        }
        return fake_rates.get(rate)


# --- TEST ---
if __name__ == "__main__":
    user = User(session="xxx", ip="192.167.0.0", client_id="yyy")
    api = WiseApi(rate_limiter=RateLimiter(max_requests=5, default_ttl=60))

    for i in range(10):
        try:
            result = api.get_rate(user, "GBP_USD")
            print(f"Request {i}: {result}")
        except TooManyRequestException as e:
            print(f"Request {i}: BLOCKED — {e}")
