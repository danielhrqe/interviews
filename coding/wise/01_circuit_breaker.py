"""
WISE PAIR PROGRAMMING — Problem 1: Circuit Breaker

SCENARIO:
You work at Wise. Your WebClient sends money to partner banks via API.
Last week, one partner bank went down for 20 minutes. During that time,
your system kept sending thousands of requests to a dead service, causing:
- Timeout cascade across microservices
- Thread pool exhaustion
- Users couldn't send money even to OTHER healthy banks

RULES:
- If a service fails 3 times within 10 minutes → stop sending requests (OPEN)
- After 5 minutes of cooldown → allow ONE request through (HALF_OPEN)
- If that request succeeds → resume normal (CLOSED)
- If it fails → back to OPEN for another 5 minutes
"""

from datetime import datetime, timedelta


class CircuitBreakerOpenError(Exception):
    """Raised when circuit is OPEN and requests are blocked."""
    pass

class CircuitBreakerServiceNotExists(Exception):
    pass

class CircuitBreaker:
    CLOSED = "CLOSED"
    OPEN = "OPEN"
    HALF_OPEN = "HALF_OPEN"

    def __init__(self):
        self.services = {
            "bank_hsbc":{
                    "failure_threshold": 3,
                    "failure_window": 600,
                    "cooldown": 300,
                    "state": self.CLOSED,
                    "failures": [],
                    "opened_at": None,
            },
            "bank_nigeria":{
                    "failure_threshold": 1,
                    "failure_window": 600,
                    "cooldown": 300,
                    "state": self.CLOSED,
                    "failures": [],
                    "opened_at": None,
            },
            "bank_brazil":{
                    "failure_threshold": 10,
                    "failure_window": 600,
                    "cooldown": 300,
                    "state": self.CLOSED,
                    "failures": [],
                    "opened_at": None,
            },
        }

    def _get_service(self, service_name):
        if service_name not in self.services:
            raise CircuitBreakerServiceNotExists()

        return self.services[service_name]

    def allow_request(self, service_name):
        """Check if a request is allowed to go through."""
        service = self._get_service(service_name)

        if service["state"] == self.CLOSED:
            return True

        if service["state"] == self.OPEN:
            # Check if cooldown period has passed
            if datetime.now() - service["opened_at"] >= timedelta(seconds=service["cooldown"]):
                service["state"] = self.HALF_OPEN
                return True  # allow ONE request to test
            return False  # still cooling down

        if service["state"] == self.HALF_OPEN:
            return False  # already let one through, waiting for result

        return False

    def record_success(self, service_name):
        """Called when a request succeeds."""
        service = self._get_service(service_name)
        if service["state"] == self.HALF_OPEN:
            # Test request succeeded — service is back!
            service["state"] = self.CLOSED
            service["failures"] = []
            service["opened_at"] = None

    def record_failure(self, service_name):
        """Called when a request fails."""
        service = self._get_service(service_name)
        now = datetime.now()

        if service["state"] == self.HALF_OPEN:
            # Test request failed — back to OPEN
            service["state"] = self.OPEN
            service["opened_at"] = now
            return

        # CLOSED state: record failure and check threshold
        service["failures"].append(now)

        # Remove failures outside the time window
        cutoff = now - timedelta(seconds=service["failure_window"])
        service["failures"] = [t for t in service["failures"] if t > cutoff]

        # Check if we hit the threshold
        if len(service["failures"]) >= service["failure_threshold"]:
            service["state"] = self.OPEN
            service["opened_at"] = now


class WebClient:
    def __init__(self, circuit_breaker=None):
        self.circuit_breaker = circuit_breaker or CircuitBreaker()

    def execute(self, service_name: str, request: str) -> str:
        # Step 1: Ask circuit breaker if we can proceed
        if not self.circuit_breaker.allow_request(service_name):
            raise CircuitBreakerOpenError(
                f"{service_name} is unavailable. Circuit is OPEN."
            )

        # Step 2: Try the request
        try:
            response = self._do_request(request)
            self.circuit_breaker.record_success(service_name)
            return response
        except Exception as e:
            self.circuit_breaker.record_failure(service_name)
            raise e

    def _do_request(self, request: str) -> str:
        """Actual HTTP call. Separated for testability."""
        import requests
        response = requests.get(request)
        response.raise_for_status()
        return response.text


# --- USAGE EXAMPLE ---
if __name__ == "__main__":
    client = WebClient()

    # Simulating requests to a failing bank
    for i in range(5):
        try:
            result = client.execute("bank_hsbc", "https://api.hsbc.com/transfer")
            print(f"Request {i}: OK")
        except CircuitBreakerOpenError as e:
            print(f"Request {i}: BLOCKED — {e}")
        except Exception as e:
            print(f"Request {i}: FAILED — {e}")
